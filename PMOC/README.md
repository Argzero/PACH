TO SET UP, FOLLOW THESE INSTRUCTIONS
1. Make sure you have python installed 
	- on mac in terminal or windows in powershell type python and see if it tells you a version number. If not, get the binaries from the python site
2. Make sure you get LibAV and FFMPEG libraries installed.
# NOTE: You will need Homebrew (*if you dont have it, easy quick fix)
run the below line in terminal
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

on mac this is:
3a. # libav
brew install libav --with-libvorbis --with-sdl --with-theora

3b. # ffmpeg
brew install ffmpeg --with-libvorbis --with-ffplay --with-theora

# NOTE THAT THE ABOVE STEP WILL TAKE SEVERAL MINUTES; PLEASE BE PATIENT

TO USE THIS FOLLOW THESE INSTRUCTIONS
1. Put the PMOC Folder in the directory of the files you wish to convert
2. cd to the directory containing the folder PMOC and run "python PMOC"
3. the new mp3 and ogg files should be sitting in the same folder as the aiff/wav files

