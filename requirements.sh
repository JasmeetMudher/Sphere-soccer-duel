#!/bin/bash

# Install Python3 and pip3 (if not already installed)
echo "Installing Python3 and pip3..."
sudo apt-get install -y python3 python3-pip

# Install the 'curses' library for Windows (if needed)
if [[ "$OSTYPE" == "msys" ]]; then
    echo "Installing windows-curses for Windows..."
    pip3 install windows-curses
else
    echo "Curses library is usually pre-installed on Unix-based systems."
fi

echo "Installation complete. You are ready to run Sphere Soccer Duel."
