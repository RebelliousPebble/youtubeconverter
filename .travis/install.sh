#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    brew update
    brew outdates xctool || brew upgrade xctool
    brew upgrade python
    pip3 install pyqt5 requests pytube imageio pyinstaller git+https://github.com/RebelliousPebble/moviepy.git
else
    sudo apt-get install python3 python3-pip
    pip3 install requests pytube imageio pyinstaller pyqt5 sip git+https://github.com/RebelliousPebble/moviepy.git
fi


