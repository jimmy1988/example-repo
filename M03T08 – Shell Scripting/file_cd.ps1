# This script creates main folders and sub-folders in the current directory.


# Define the main folders to be created
$mainFolders = "main_folder1", "main_folder2", "main_folder3"

# Define the sub-folders to be created within each main folder
$subFolders = "sub_folder1", "sub_folder2", "sub_folder3"

# Loop through each main folder and create it if it doesn't exist
foreach ($folder in $mainFolders) {
    #Set the current directory to the script's location
    Set-Location -Path $PSScriptRoot

    $path = Join-Path -Path (Get-Location) -ChildPath $folder

    # Create the main folder if it doesn't exist
    if (-not (Test-Path -Path $path -PathType Container)) {
        New-Item -ItemType Directory -Path $path | Out-Null
        Write-Host "Main Folder created successfully." -ForegroundColor Green
    } else {
        Write-Host "Main Folder already exists." -ForegroundColor Yellow
    }

    # Change the current directory to the newly created main folder
    Set-Location -Path $PSScriptRoot/$folder

    # Loop through each sub-folder and create it if it doesn't exist
    foreach ($subFolder in $subFolders) {
        $subPath = Join-Path -Path (Get-Location) -ChildPath $subFolder

        if (-not (Test-Path -Path $subPath -PathType Container)) {
            New-Item -ItemType Directory -Path $subPath | Out-Null
            Write-Host "Sub-folder created successfully." -ForegroundColor Green
        } else {
            Write-Host "Sub-folder already exists." -ForegroundColor Yellow
        }
    }
}

#Set the current directory to the script's location
Set-Location -Path $PSScriptRoot

# 1. Define your base directory containing the main folders
$basePath = $PSScriptRoot

# 2. Select exactly ONE random main folder
$randomMainFolder = Get-ChildItem -Path $basePath -Directory | Get-Random

if ($null -ne $randomMainFolder) {
    Write-Host "Selected Main Folder: $($randomMainFolder.FullName)" -ForegroundColor Cyan

    # 3. Get all subfolders inside that selected main folder
    $subFolders = Get-ChildItem -Path $randomMainFolder.FullName -Directory

    # 4. Pick up to 2 random subfolders from the list
    # (Using -Count 2 handles cases where there might only be 1 or 2 folders total without crashing)
    $subFoldersToDelete = $subFolders | Get-Random -Count 2

    # 5. Delete them loop-style
    foreach ($folder in $subFoldersToDelete) {
        Write-Host "Deleting subfolder: $($folder.Name)" -ForegroundColor Yellow
        
        # -Recurse deletes contents; -Force handles hidden/read-only items
        Remove-Item -Path $folder.FullName -Recurse -Force
    }
} else {
    Write-Warning "No main folders found in the specified base directory."
}
