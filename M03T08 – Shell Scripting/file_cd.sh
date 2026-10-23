#!/bin/bash

# Get the absolute path of the directory where this script is located
SCRIPT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Define the main folders and sub-folders to be created
MAIN_FOLDERS=("main_folder1" "main_folder2" "main_folder3")
SUB_FOLDERS=("sub_folder1" "sub_folder2" "sub_folder3")

# --- PART 1: CREATE FOLDERS ---

# Loop through each main folder
for folder in "${MAIN_FOLDERS[@]}"; do
    # Set the current directory to the script's location
    cd "$SCRIPT_ROOT" || exit

    # Define paths safely using arrays or variables
    path="$SCRIPT_ROOT/$folder"

    # Create the main folder if it doesn't exist
    if [ ! -d "$path" ]; then
        mkdir -p "$path"
        echo -e "\e[32mMain Folder created successfully.\e[0m" # Green text
    else
        echo -e "\e[33mMain Folder already exists.\e[0m" # Yellow text
    fi

    # Change the current directory to the main folder
    cd "$path" || exit

    # Loop through each sub-folder and create it if it doesn't exist
    for subFolder in "${SUB_FOLDERS[@]}"; do
        if [ ! -d "$path/$subFolder" ]; then
            mkdir -p "$path/$subFolder"
            echo -e "\e[32mSub-folder created successfully.\e[0m" # Green text
        else
            echo -e "\e[33mSub-folder already exists.\e[0m" # Yellow text
        fi
    done
done

# --- PART 2: RANDOM SELECTION & DELETION ---

# Reset directory to script location
cd "$SCRIPT_ROOT" || exit
basePath="$SCRIPT_ROOT"

# Select exactly ONE random main folder directory
# (find lists directories, grep filters out the root, shuf randomly shuffles them, head picks the first)
randomMainFolder=$(find "$basePath" -maxdepth 1 -mindepth 1 -type d | shuf -n 1)

if [ -n "$randomMainFolder" ]; then
    echo -e "\e[36mSelected Main Folder: $(basename "$randomMainFolder")\e[0m" # Cyan text

    # Map all subfolders inside the chosen directory into an array
    # Using readarray to prevent splitting issues on folders with spaces
    readarray -t subFolders < <(find "$randomMainFolder" -maxdepth 1 -mindepth 1 -type d)

    # Count how many subfolders actually exist
    subFolderCount=${#subFolders[@]}

    if [ "$subFolderCount" -gt 0 ]; then
        # Pick up to 2 random subfolders from the array using shuf
        # We loop through the elements passed by shuf and limit the count to 2
        printf '%s\n' "${subFolders[@]}" | shuf -n 2 | while read -r folderToDelete; do
            if [ -n "$folderToDelete" ]; then
                echo -e "\e[33mDeleting subfolder: $(basename "$folderToDelete")\e[0m" # Yellow text
                
                # rm -rf handles recursive deletion and forces past minor prompts
                rm -rf "$folderToDelete"
            fi
        done
    else
        echo "No sub-folders found inside the selected main folder to delete."
    fi
else
    echo -e "\e[33mWarning: No main folders found in the specified base directory.\e[0m"
fi
