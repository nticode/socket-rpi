#!/bin/bash

echo "Installing Python3"
exec sudo apt-get install python3
echo "Python3 Installed"

echo "Installing Packages"
exec pip install -r requirements.txt
echo "Packages Installed"
