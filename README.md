# qr-code-maker-saver
# QR Code Generator for ChronoDrive Quest - README

## Overview
The QR Code Generator is an integral tool for the "ChronoDrive Quest" game, enabling the creation of QR codes from user-inputted alphanumeric text. This tool streamlines the process of transferring data within the gaming environment, offering a convenient method for players to interact with various game elements through QR codes.

## Features
- **Efficient QR Code Creation**: Generates QR codes from user-entered text.
- **Automatic File Saving**: Saves QR code images and corresponding text in a specific folder.
- **Sanitized Filenames**: Generates valid file names based on the input text for system compatibility.

## Requirements
- Python 3.x
- Tkinter (typically included with Python)
- Python Imaging Library (PIL)
- qrcode Python library

## Installation
Install the required libraries with pip:
```bash
pip install pillow qrcode
```

## Usage
Launch the tool, enter text in the GUI, and click 'Drive Quest' to generate and save QR codes. QR codes will be displayed in the GUI and saved in the 'QR_codes' folder.

## File Structure
- QR codes and text files are saved in the `QR_codes` folder.
- Filenames are based on the input text, sanitized for compatibility.

## Error Handling
Basic error handling for invalid inputs and file system errors, with message boxes displaying error details.

## Customization
Customizable parameters include folder name, QR code size, and error correction level.

## Support
For support or to report bugs, please email echoesofthechronodrive@gmail.com.

This README offers a concise guide for the QR Code Generator specifically tailored for the ChronoDrive Quest game. For further modifications or enhancements, feel free to contribute to this project.
The user enters text and clicks the 'Drive Quest' button, the program generates a QR code that represents the entered text. This QR code is then displayed in the GUI. Both the QR code and the text are saved in the 'QR_codes' folder. The filenames are based on the input text.
