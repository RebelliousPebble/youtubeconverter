#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    brew update
    brew outdates xctool || brew upgrade xctool
    brew install python36
    sudo pip3 install pyqt5 moviepy requests pytube movieio
else
    sudo apt get install python36
    sudo pip install pyqt5 moviepy requests pytube movieio
fi


