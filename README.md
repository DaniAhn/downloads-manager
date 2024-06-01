# Downloads Manager
This python script allows you to manage the files in your Downloads folder. It automatically creates a folder structure and has the option to sort your files based on their file extension. It also has the option to clear a specific folder by moving all contained files to the Recycle Bin, or to clear all folders in the organization structure.
## Getting Started
### Installing
- Install the required Python library by running:
```
pip install send2trash
```
### Folder Structure
This script creates the following organization structure, where files are sorted into the corresponding folder based on file extension.
- Audio: .mp3, .wav, .m4a, .wma, .ogg, .mid, .midi
- Documents: .txt, .pdf, .docx, .odt, .rtf, .epub, .pptx
- Photos: .jpg, .png, .webp, .gif, .jpeg, .bmp, .svg
- Videos: .mp4, .webm, .wmv, .mkv, .mov, .mpeg, .mpg
- Executables: .bat, .bin, .exe, .msi, .sh, .wsf
- Compressed: .7z, .zip, .rar, .arj, .pkg
- Other: Files that do not match any of the above

The above folder structure is automatically created the first time the program is run, and any missing folders will be replaced on subsequent executions. Directories are ignored and remain in the Downloads folder.
### Executing Program
#### Sort Files
Sort files in your Downloads folder by running:
```
python downloads-manager.py sort
```
#### Clear Folders
Clear the desired folder by runnning:
```
python downloads-manager.py clear <folder_name|All>
```
The folder name is case-sensitive. The selected folder will be completely emptied into the recycle bin. If All is selected, the script will empty all of the folders in the organization structure.
## Authors
Daniel Ahn
