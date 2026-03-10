<p align="center">
  <img src="https://i.imgur.com/ZXrc1ma.jpeg" width="600" alt="Banner">
</p>

# SortGdrive
An automated Python script to neatly upload and sort files from local storage to Google Drive based on file extension.

## Key features
1. Flexible code: can be used on any device (Android, Linux, max os, windows)
2. Auto-Categorization: Sort files into custom folders (Documents, Images, Videos, etc.) in Google Drive.
3. Cloud Integration: Connect directly using the Google Drive API or rclone.
4. Customizable: Easily add new file extensions through a configuration file.

## Workflow
1. Scanning: The script scans the input source folder on the device.
2. Filtering: Files are grouped by extension (eg: .jpg to Images folder).
3. Uploading: The process of moving files from the device to Google Drive

## 🛠️ Step-by-Step Installation
Choose the guide below based on the device you are using.

### 🪟 1. Windows Users

1. **Install Python:** Download it from [python.org](https://www.python.org/downloads/). During installation, **YOU MUST** check the box that says **"Add Python to PATH"**.
2. **Install Git:** Download and install [Git for Windows](https://git-scm.com/download/win). Simply click 'Next' until the setup is finished.
3. **Open Terminal:** Press the `Windows` key, type **PowerShell**, and hit Enter.
4. **Run these commands:**
   ```powershell
   git clone [https://github.com/Alprisz10/sortGdrive](https://github.com/Alprisz10/sortGdrive)
   cd sortGdrive
   pip install -r requirements.txt
   python main.py
<br>

### 🐧 2. Linux Users (Ubuntu/Debian/Lubuntu)
Open your Terminal (Ctrl+Alt+T) and run these commands one by one:

1. **Update & Install Tools:**
```Bash
sudo apt update && sudo apt upgrade -y
sudo apt install git python3 python3-pip python3-venv -y
```
2. **Clone & Run:**
```Bash
git clone [https://github.com/Alprisz10/sortGdrive](https://github.com/Alprisz10/sortGdrive)
cd sortGdrive
pip3 install -r requirements.txt
python3 main.py
```
<br>

### 🤖 3. Android Users (Via Termux)
Please install Termux from F-Droid (not the Play Store version).

1. **Grant Storage Access:**
```Bash
termux-setup-storage
```
(Click "Allow" when the pop-up appears on your phone screen)
2. **Update & Install Packages:**
```Bash
pkg update && pkg upgrade -y
pkg install git python -y
```
3. **Clone & Run:**
```Bash
git clone [https://github.com/Alprisz10/sortGdrive](https://github.com/Alprisz10/sortGdrive)
cd sortGdrive
pip install -r requirements.txt
python main.py
```
<br>

### 🍎 4. macOS Users

1.**Install Homebrew**  (if not already installed):

Visit brew.sh and follow the instructions.

2. **Install Python & Git:**

```Bash

brew install python git

```

3. **Clone & Run:**

```Bash

git clone [https://github.com/Alprisz10/sortGdrive](https://github.com/Alprisz10/sortGdrive)cd sortGdrive

pip3 install -r requirements.txt

python3 main.py

```
