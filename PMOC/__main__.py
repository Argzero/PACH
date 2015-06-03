import os,sys
from lib.pydub import AudioSegment

def main():
  path = os.path.abspath(__file__)+"../../../"
  dirs = os.listdir(path)
  for file in dirs:
    if file.endswith("wav"):
      print file
    elif file.endswith("aiff"):
      print "AIFFF!!!"
  return
if __name__ == '__main__':
  main()