TO USE THIS FOLLOW THESE INSTRUCTIONS
1. Put the PMOC Folder in the directory of the files you wish to convert
2. Make sure you have python installed 
	- on mac in terminal or windows in powershell type python and see if it tells you a version number. If not, get the binaries from the python site
3. Make sure you get LibAV and FFMPEG libraries installed.

on mac this is:
# libav
brew install libav --with-libvorbis --with-sdl --with-theora

# ffmpeg
brew install ffmpeg --with-libvorbis --with-ffplay --with-theora

4. cd to the directory containing the folder PMOC and run "python PMOC"
5. the new mp3 and ogg files should be sitting in the same folder