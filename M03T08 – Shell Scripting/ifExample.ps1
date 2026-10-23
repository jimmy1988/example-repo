# Check if 'new_folder' exists, and if so, create 'if_folder'
if (Test-Path -Path "new_folder" -PathType Container) {
    New-Item -ItemType Directory -Path "if_folder" -Force | Out-Null
}

# Check if 'if_folder' exists; if it does, create 'hyperionDev', else create 'new-projects'
if (Test-Path -Path "if_folder" -PathType Container) {
    New-Item -ItemType Directory -Path "hyperionDev" -Force | Out-Null
} else {
    New-Item -ItemType Directory -Path "new-projects" -Force | Out-Null
}
