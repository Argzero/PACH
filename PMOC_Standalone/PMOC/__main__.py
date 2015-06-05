import os,sys
from collections import defaultdict
import time
from pydub import AudioSegment

def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch
getch = _find_getch()

os.system('cls' if os.name == 'nt' else 'clear')

abspath = os.path.abspath(raw_input("Please provide the folder of the audio files you wish\nto convert.\n\n"))
dirs = os.listdir(abspath)
os.chdir(abspath)
wavs = []
aiffs = []
mp3s = []
oggs = []
_mp3s = None
_oggs = None 

file_type = defaultdict(str) # sfx, sfx-r, music, voice, voice-om
file_info = defaultdict(lambda : defaultdict(str))

music = {'bitrate':'96k'}
sfx_range = {'bitrate':'96k'}
sfx = {'bitrate':'64k'}
voice_alone = {'bitrate':'96k'}
voice_over_music = {'bitrate':'64k'}

def get_bitrate(hashmap):
  return hashmap['bitrate']
def get_params(hashmap):
  return hashmap['bitrate']
def get_info_for_type(type):
  global music
  global sfx
  global sfx_range
  global voice_alone
  global voice_over_music
  info = {}
  if(type == "music"):
    info['bitrate'] = get_bitrate(music)
  elif(type == "sfx-r"):
    info['bitrate'] = get_bitrate(sfx_range)
  elif(type == "sfx"):
    info['bitrate'] = get_bitrate(sfx)
  elif(type == "voice"):
    info['bitrate'] = get_bitrate(voice_alone)
  elif(type == "voice-om"):
    info['bitrate'] = get_bitrate(voice_over_music)
  return info

def infer_type(name):
  global getch
  assumed_type = "unknown"
  if 'sfx' in name:
    assumed_type = 'sfx'
  elif 'music' in name:
    assumed_type = 'music'
  elif 'voice' in name:
    assumed_type = 'voice'
  if assumed_type == "unknown":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("TYPE UNCERTAIN FOR FILE\n\n"+name+"\n\nPlease Provide the type by pressing one of the characters below:\n\n  1: Music\n  2: SFX\n  3. Voice\n\n")
    user_input = getch()
    if user_input == '1':
      assumed_type = 'music'
    elif user_input == '2':
      assumed_type = 'sfx' 
    elif user_input == '3':
      assumed_type = 'voice' 
      
  if assumed_type == 'sfx':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(name + "\n\n")
    print("Does this SFX have a large range of pitches?\nPlease Provide the type by pressing one of the characters below:\n\n  1: Yes\n  2: No\n\n")
    user_input = getch()
    if user_input == '1':
      assumed_type = 'sfx-r'
    elif user_input == '2':
      assumed_type = 'sfx' 
  if assumed_type == 'voice':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(name + "\n\n")
    print("Does this voice play over music or by itself?\nPlease Provide the type by pressing one of the characters below:\n\n  1: Plays over Music\n  2: Plays Alonen\n")
    user_input = getch()
    if user_input == '1':
      assumed_type = 'voice-om'
    elif user_input == '2':
      assumed_type = 'voice' 
  return assumed_type

def check_info(name):
  global file_info
  global file_type
  os.system('cls' if os.name == 'nt' else 'clear')
  if file_type[name] == 'unknown':
    file_type[name] = infer_type(name)
    file_info[name] = get_info_for_type(file_type[name])
    print("Is " + name + " Mono?\n\n  1: Mono\n  2: Not Mono");
    user_input = getch()
    channel_count = 1 if user_input=='1' else 2
    if channel_count == 1:
      (file_info[name])['parameters'] = ["-ac", "1"] # sets it to mono audio
    else:
      (file_info[name])['parameters'] = []
    return file_info[name]
  else:
    return file_info[name]

def wav_to_mp3(name):
  print name + "\n  : # .wav found\n  : # converting to mp3"
  global _mp3s
  global abspath
  _export_name = os.path.splitext(name)[0]
  info = check_info(_export_name)
  if name in _mp3s:
    print name + " MP3 EXISTS"
    getch()
    return 1
  else:
    print name + " MP3 CREATING"
    _song = AudioSegment.from_wav(abspath+"/"+name)
    _song.export(_export_name + ".mp3", format="mp3", bitrate=get_bitrate(info), parameters=get_params(info))
    print name + " MP3 CREATED"
    return 0
def aiff_to_mp3(name):
  print name + "\n  : # .aiff found\n  : # converting to mp3"
  global _mp3s
  global abspath
  _export_name = os.path.splitext(name)[0]
  info = check_info(_export_name)
  if name in _mp3s:
     print name + " MP3 EXISTS"
     getch()
     return 1
  else:
    _song = AudioSegment.from_file(abspath+"/"+name,"aac")
    _song.export(_export_name + ".mp3", format="mp3", bitrate=get_bitrate(info), parameters=get_params(info))
    print name + " MP3 CREATED"
    return 0 
def ogg_to_mp3(name):
  print name + "\n  : # .ogg found\n  : # converting to mp3"
  global _mp3s
  global abspath
  _export_name = os.path.splitext(name)[0]
  info = check_info(_export_name)
  if name in _mp3s:
     print name + " MP3 EXISTS"
     getch()
     return 1
  else:
    _song = AudioSegment.from_ogg(abspath+"/"+name)
    _song.export(_export_name + ".mp3", format="mp3", bitrate=get_bitrate(info), parameters=get_params(info))
    print name + " MP3 CREATED"
    return 0
def wav_to_ogg(name):
  print name + "\n  : # .wav found\n  : # converting to ogg"
  global _oggs
  global abspath
  _export_name = os.path.splitext(name)[0]
  info = check_info(_export_name)
  if name in _oggs:
    print name + " OGG EXISTS\n\npress any key to continue..."
    getch()
    return 0
  else:
    _song = AudioSegment.from_wav(abspath+"/"+name)
    _song.export(_export_name + ".ogg", format="ogg", bitrate=get_bitrate(info), parameters=get_params(info))
    print name + " OGG CREATED"
    return  
def aiff_to_ogg(name):
  print name + "\n  : # .aiff found\n  : # converting to ogg"
  global _oggs
  global abspath
  _export_name = os.path.splitext(name)[0]
  info = check_info(_export_name)
  if name in _oggs:
    print name + " OGG EXISTS\n\npress any key to continue..."
    getch()
    return
  else:
    _song = AudioSegment.from_file(abspath+"/"+name,"aac")
    _song.export(_export_name + ".ogg", format="ogg", bitrate=get_bitrate(info), parameters=get_params(info))
    print name + " OGG CREATED"
    return 
def mp3_to_ogg(name):
  print name + "\n  : # .mp3 found\n  : # converting to ogg"
  global _oggs
  global abspath
  _export_name = os.path.splitext(name)[0]
  info = check_info(_export_name)
  if name in _oggs:
    print name + " OGG EXISTS\n\npress any key to continue..."
    getch()
    return 0
  else:
    _song = AudioSegment.from_mp3(abspath+"/"+name)
    _song.export(_export_name + ".ogg", format="ogg", bitrate=get_bitrate(info), parameters=get_params(info))
    print name + " OGG CREATED"
    return
    
def main():
  global dirs
  global _mp3s
  global _oggs
  global mp3s
  global oggs
  global wavs
  global aiffs
  for file in dirs:
    file_type[file] = "unknown"
    file_info[file] = {}
    if file.endswith("wav"):
      wavs.append(file)
    elif file.endswith("aiff"):
      print file + "\n  : # .aiff found\n  : # converting to mp3 and ogg"
      aiffs.append(file)
    elif file.endswith("mp3"):
      print file + "\n  : # .mp3 found"
      mp3s.append(file)  
    elif file.endswith("ogg"):
      print file + "\n  : # .ogg found"
      oggs.append(file) 
  _mp3s = set(mp3s)    
  _oggs = set(oggs)  
  
  for wav in wavs:
    os.system('cls' if os.name == 'nt' else 'clear')
    wav_to_mp3(wav)
    wav_to_ogg(wav)
  for aiff in aiffs:
    os.system('cls' if os.name == 'nt' else 'clear')
    aiff_to_mp3(aiff)
    aiff_to_ogg(aiff)
  for mp3 in mp3s:
    os.system('cls' if os.name == 'nt' else 'clear')
    mp3_to_ogg(mp3)
  for ogg in oggs:
    os.system('cls' if os.name == 'nt' else 'clear')
    ogg_to_mp3(ogg)
  print "COMPLETED SUCCESSFULLY"
  time.sleep(3)
  return 0
if __name__ == '__main__':
  main()