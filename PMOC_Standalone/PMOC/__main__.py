import os,sys
import time
from pydub import AudioSegment
import os
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

file_type = {} # 'sfx':'sfx', 'music':'music', 'voice':'voice'
file_info = {}

music = {'bitrate':128000}
sfx_range = {'bitrate':96000}
sfx = {'bitrate':64000}
voice_alone = {'bitrate':96000}
voice_over_music = {'bitrate':64000}

def get_bitrate(hashmap):
  return hashmap['bitrate']
  
def get_info_for_type(type):
  global music
  global sfx
  global sfx_range
  global voice_alone
  global voice_over_music
  if(type == "music")
    return music
  if(type == "sfx-r")
    return music
  if(type == "sfx")
    return music
  if(type == "music")
    return music
    
def infer_type(name):
  if 'sfx' in name:
    return 'sfx'
  if 'music' in name:
    return 'music'
  if 'voice' in name:
    return 'voice'
  return 'unknown'

def check_info(name):
  global file_info
  global file_type
  os.system('cls' if os.name == 'nt' else 'clear')
  if file_type[name] == 'unknown':
    channel_count = (input("Mono?\n1: Mono\n2: Not Mono")==1)? 1: 2)
    if channel_count == 1:
      (file_info[name])[parameters] = ["-ac", "1"] # sets it to mono audio
    else:
      (file_info[name])[parameters] = []
    file_type[name] = infer_type(name)
    
    return file_info[name]
  else:
    return file_info[name]

def wav_to_mp3(name):
  print name + "\n  : # .wav found\n  : # converting to mp3"
  global _mp3s
  global abspath
  if name in _mp3s:
    print name + " MP3 EXISTS"
    return 1
  else:
    print name + " MP3 CREATING"
    _song = AudioSegment.from_wav(abspath+"/"+name)
    _export_name = os.path.splitext(name)[0]
    _song.export(_export_name + ".mp3", format="mp3")
    print name + " MP3 CREATED"
    return 0
def aiff_to_mp3(name):
  print name + "\n  : # .aiff found\n  : # converting to mp3"
  global _mp3s
  global abspath
  if name in _mp3s:
     print name + " MP3 EXISTS"
     return 1
  else:
    _song = AudioSegment.from_file(abspath+"/"+name,"aac")
    _export_name = os.path.splitext(name)[0]
    _song.export(_export_name + ".mp3", format="mp3")
    print name + " MP3 CREATED"
    return 0

def wav_to_ogg(name):
  print name + "\n  : # .wav found\n  : # converting to ogg"
  global _oggs
  global abspath
  if name in _oggs:
    	print name + " OGG EXISTS"
    	return 0
  else:
    _song = AudioSegment.from_wav(abspath+"/"+name)
    _export_name = os.path.splitext(name)[0]
    _song.export(_export_name + ".ogg", format="ogg")
    print name + " OGG CREATED"
    return
    
def ogg_to_mp3(name):
  print name + "\n  : # .ogg found\n  : # converting to mp3"
  global _mp3s
  global abspath
  if name in _mp3s:
     print name + " MP3 EXISTS"
     return 1
  else:
    _song = AudioSegment.from_ogg(abspath+"/"+name)
    _export_name = os.path.splitext(name)[0]
    _song.export(_export_name + ".mp3", format="mp3")
    print name + " MP3 CREATED"
    return 0

def mp3_to_ogg(name):
  print name + "\n  : # .mp3 found\n  : # converting to ogg"
  global _oggs
  global abspath
  if name in _oggs:
    	print name + " OGG EXISTS"
    	return 0
  else:
    _song = AudioSegment.from_mp3(abspath+"/"+name)
    _export_name = os.path.splitext(name)[0]
    _song.export(_export_name + ".ogg", format="ogg")
    print name + " OGG CREATED"
    return
  
def aiff_to_ogg(name):
  print name + "\n  : # .aiff found\n  : # converting to ogg"
  global _oggs
  global abspath
  if name in _oggs:
    print name + " OGG EXISTS"
    return
  else:
    _song = AudioSegment.from_file(abspath+"/"+name,"aac")
    _export_name = os.path.splitext(name)[0]
    _song.export(_export_name + ".ogg", format="ogg")
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
    print wav
    wav_to_mp3(wav)
    wav_to_ogg(wav)
  for aiff in aiffs:
    aiff_to_mp3(aiff)
    aiff_to_ogg(aiff)
  for mp3 in mp3s:
    mp3_to_ogg(mp3)
  for ogg in oggs:
    ogg_to_mp3(ogg)
  print "COMPLETED SUCCESSFULLY"
  time.sleep(6)
  return 0
if __name__ == '__main__':
  main()