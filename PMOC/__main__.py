import os,sys
import time
from pydub import AudioSegment

path = os.path.dirname(sys.argv[0])
abspath = os.path.abspath(path)
dirs = os.listdir(abspath)
wavs = []
aiffs = []
mp3s = []
oggs = []
_mp3s = None
_oggs = None 

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
  print "COMPLETED SUCCESSFULLY"
  time.sleep(6)
  return 0
if __name__ == '__main__':
  main()