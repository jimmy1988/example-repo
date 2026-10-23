#!/bin/bash

# Check if 'new_folder' exists, and if so, create 'if_folder'
if [ -d "new_folder" ]; then
    mkdir -p "if_folder"
fi

# Check if 'if_folder' exists; if it does, create 'hyperionDev', else create 'new-projects'
if [ -d "if_folder" ]; then
    mkdir -p "hyperionDev"
else
    mkdir -p "new-projects"
fi
