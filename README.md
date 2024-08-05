# Downloads Manager
This python script allows you to manage the files in your Downloads folder. It automatically creates a folder structure to organize your files, and is able to sort your downloads based on their file extension. It also has the option to clear the contents of each folder by moving them to the Recycle Bin.

## Getting Started
### Installation
Install the required Python library by running the following command in the terminal window:
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

The above folder structure is automatically created the first time the program is run, and any missing folders within the structure will be replaced on subsequent executions. Any folders that are not part of the structure are ignored and remain in the Downloads folder.

### Executing Program
#### Sort Files
Sort files in your Downloads folder by running:
```
python downloads-manager.py sort
```
#### Clear Folders
Clear the desired folder by runnning:
```
python downloads-manager.py clear <folder name>
```
The submitted folder will be completely emptied into the Recycle Bin. The folder name is case-sensitive.

Alternatively, run the following command:
```
python downloads-manager.py clear All
```
Running this command will cause the script to empty all of the folders in the organization structure into the Recycle Bin.

## Authors
Daniel Ahn
