#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    brew update
    brew outdates xctool || brew upgrade xctool
    brew upgrade python
    sudo pip3 install pyqt5 requests pytube imageio pyinstaller git+https://github.com/RebelliousPebble/moviepy.git
    export PATH=$PATH:/Users/travis/Library/Python/3.7/bin
    echo $PATH
else
    sudo apt-get install python3 python3-pip
    pip3 install requests pytube imageio pyinstaller pyqt5 sip git+https://github.com/RebelliousPebble/moviepy.git
fi


