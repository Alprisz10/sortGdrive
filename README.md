<p align="center">
  <img src="https://i.imgur.com/ZXrc1ma.jpeg" width="700" alt="SortGdrive Banner - Organize your cloud effortlessly">
</p>

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS%20%7C%20Android-lightgrey?style=for-the-badge" alt="Platform Support">
  </a>
  <a href="https://github.com/Alprisz10/sortGdrive/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  </a>
  <a href="https://github.com/Alprisz10/sortGdrive/issues">
    <img src="https://img.shields.io/github/issues/Alprisz10/sortGdrive?style=for-the-badge" alt="Open Issues">
  </a>
</p>

---

# 📁 SortGdrive: The Neat Freak's Google Drive Uploader

Tired of a messy cloud storage? **SortGdrive** is an intelligent, cross-platform Python script that automates the process of uploading and sorting your local files directly into neatly organized folders on Google Drive using **rclone**.

It acts as a smart bridge between your device and the cloud, scanning a specified folder and categorizing your files (like Photos, Videos, Documents, and more) based on their extensions. No more manual folder creation or dragging and dropping!

---

## ✨ Key Features

*   **🌐 Truly Cross-Platform:** One codebase to rule them all. Works flawlessly on **Windows, Linux, macOS, and even Android (via Termux)**.
*   **🤖 Intelligent Auto-Categorization:** Automatically sorts files into 8 custom folders in your Google Drive:
    - 📄 Documents/Word_Processing
    - 📊 Documents/Spreadsheets
    - 📽️ Documents/Presentation
    - 🗜️ Documents/Archives
    - 🖼️ Photos
    - 🎬 Videos
    - 🎵 Audios
    - 💻 Applications
*   **🔌 Powered by rclone:** Uses the reliable and fast `rclone` for cloud transfers with automatic installation if not present.
*   **🔄 Automatic Remote Creation:** Script automatically creates and manages the `sortGdrive` remote for you.
*   **📁 Flexible Input:** Choose between the default `Move_dir` folder or specify any custom directory on your device.
*   **🛡️ Auto-Folder Creation:** Automatically creates all necessary folders in your Google Drive before uploading.

---

## 🗺️ How It Works: The Workflow

1.  **🔍 Scan:** The script scans either the default `Move_dir` folder or a custom folder you specify.
2.  **🏷️ Filter & Categorize:** It identifies each file's extension and maps it to one of 8 predefined categories.
3.  **📂 Auto-Create Folders:** Before uploading, it ensures all destination folders exist in your Google Drive.
4.  **☁️ Upload & Organize:** The files are then moved to their respective folders using `rclone`.

```
[Your Device Folder] --> [SortGdrive] --> [Google Drive]
     (Scan)              (Categorize)        (Organized)
          └── .docx ────────┐
          └── .jpg ─────┐   └──> 📁 Documents/Word_Processing
          └── .mp4 ──┐  └───────> 📁 Photos
                     └──────────> 📁 Videos
```

---

## 📂 Folder Structure

```
sortGdrive/
├── Move_Dir/            # Default directory for file sorting (create this folder)
├── main.py              # Main script to run
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── .gitignore           # Files to ignore in Git
```

**Note:** Create the `Move_Dir` folder in the same directory as `main.py` before running the script.

---

## 🗂️ File Categorization Rules

| Category | Folder in Google Drive | File Extensions |
|----------|------------------------|-----------------|
| **Word Processing** | `Documents/Word_Processing` | .docx, .doc, .pdf, .odt, .rtf, .txt |
| **Spreadsheets** | `Documents/Spreadsheets` | .xlsx, .xls, .csv, .ods |
| **Presentations** | `Documents/Presentation` | .pptx, .ppt, .odp |
| **Archives** | `Documents/Archives` | .7z, .zip, .tar, .tar.bz2, .tar.gz, .tar.xz, .tar.lz4, .tar.zstd, .rar, .zipx |
| **Photos** | `Photos` | .jpg, .jpeg, .png, .webp, .raw, .tiff, .psd, .heic, .heif, .gif, .svg |
| **Videos** | `Videos` | .mp4, .mov, .mkv, .webm, .flv, .avi, .wmv |
| **Audios** | `Audios` | .mp3, .aac, .m4a, .wav, .flac, .ogg, .mid, .midi, .wma |
| **Applications** | `Applications` | .msi, .app, .dmg, .deb, .rpm, .bin, .run, .appimage, .ipa, .xapk, .aab, .iso, .nspro, .xci, .vpk |

---

## 🚀 Step-by-Step Installation & Setup

Choose the guide that matches your operating system.

### 🪟 1. Windows Users

1.  **Install Python:** Download the latest version from [python.org](https://www.python.org/downloads/). **CRITICAL:** During installation, **check the box** that says **"Add Python to PATH"**.
2.  **Install Git:** Download and install [Git for Windows](https://git-scm.com/download/win). Use the default settings.
3.  **Open Terminal:** Press the `Windows` key, type **PowerShell**, and hit Enter.
4.  **Run these commands:**
    ```powershell
    git clone https://github.com/Alprisz10/sortGdrive
    cd sortGdrive
    mkdir Move_Dir
    pip install -r requirements.txt
    python main.py
    ```

### 🐧 2. Linux Users (Ubuntu/Debian)

Open your Terminal (`Ctrl+Alt+T`) and run:

1.  **Update & Install Tools:**
    ```bash
    sudo apt update && sudo apt upgrade -y
    sudo apt install git python3 python3-pip -y
    ```
2.  **Clone & Run:**
    ```bash
    git clone https://github.com/Alprisz10/sortGdrive
    cd sortGdrive
    mkdir Move_Dir
    pip3 install -r requirements.txt
    python3 main.py
    ```

### 🤖 3. Android Users (Via Termux)

**Important:** Install Termux from **F-Droid** ([https://f-droid.org/en/packages/com.termux/](https://f-droid.org/en/packages/com.termux/)). The Play Store version is outdated.

1.  **Grant Storage Access:**
    ```bash
    termux-setup-storage
    ```
    (Allow the permission pop-up on your phone)
2.  **Update & Install Packages:**
    ```bash
    pkg update && pkg upgrade -y
    pkg install git python -y
    ```
3.  **Clone & Run:**
    ```bash
    git clone https://github.com/Alprisz10/sortGdrive
    cd sortGdrive
    mkdir Move_Dir
    pip install -r requirements.txt
    python main.py
    ```

### 🍎 4. macOS Users

1.  **Install Homebrew** (if not installed): Follow instructions at [brew.sh](https://brew.sh/).
2.  **Install Python & Git:**
    ```bash
    brew install python git
    ```
3.  **Clone & Run:**
    ```bash
    git clone https://github.com/Alprisz10/sortGdrive
    cd sortGdrive
    mkdir Move_Dir
    pip3 install -r requirements.txt
    python3 main.py
    ```

---

## 📖 How to Use

After installation, run the script:

```bash
python main.py   # or python3 main.py on Linux/macOS
```

You'll be greeted with a menu:

```
╔══╗╔═╗╔═╗╔══╗  ╔══╗╔══╗╔═╗╔══╗╔╗─╔╗╔═╗
║══╣║║║║╬║╚╗╔╝  ║╔═╣╚╗╗║║╬║╚║║╝║╚╦╝║║╦╝
╠══║║║║║╗╣─║║─  ║╚╗║╔╩╝║║╗╣╔║║╗╚╗║╔╝║╩╗
╚══╝╚═╝╚╩╝─╚╝─  ╚══╝╚══╝╚╩╝╚══╝─╚═╝─╚═╝
──────────────  ───────────────────────
ᴍᴀᴅᴇ ʙʏ ɴᴀᴡᴀ ᴀʟsᴀᴘʀɪsᴇ (ᴀʟᴘʀɪsᴢ)
─────────────────────────────

1. Konfigurasi ulang
2. Sortir file dari folder bawaan
3. Sortir file dari folder keinginan
masukkan pilihan :
```

### Menu Options:

| Option | Description |
|--------|-------------|
| **1. Konfigurasi ulang** | Reset and reconfigure your Google Drive connection |
| **2. Sortir file dari folder bawaan** | Sort files from the default `Move_Dir` folder |
| **3. Sortir file dari folder keinginan** | Sort files from a custom folder path |

### For Custom Folder (Option 3):
- Use `../` to navigate up from the script directory
- Example: `../../downloads/browsers`
- Or use absolute paths: `~/storage/downloads/browsers` (especially useful on Android/Termux)

---

## 🔧 First Run: Google Drive Authentication

When you run the script for the first time, rclone will prompt you to authenticate with Google Drive:

1.  The script will automatically create a remote named `sortGdrive`
2.  You'll see a URL to visit in your browser
3.  Log in to your Google account and grant permissions
4.  Copy the verification code and paste it back in the terminal
5.  Authentication is saved for future use

---

## ⚠️ Troubleshooting

### Rclone Not Found
The script automatically tries to install rclone. If it fails:

**Windows:** 
```powershell
winget install Rclone.Rclone
```

**Linux/Android:**
```bash
sudo apt install rclone          # Ubuntu/Debian
pkg install rclone                # Termux
```

**macOS:**
```bash
brew install rclone
```

### Module Not Found Errors
If you see Python module errors, ensure all dependencies are installed:

```bash
pip install -r requirements.txt --upgrade
```

### Authentication Issues
If you need to reconfigure your Google Drive connection:

1.  Run the script and select option **1 (Konfigurasi ulang)**
2.  Confirm with `y` to delete the existing remote
3.  Follow the authentication prompts again

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Alprisz10/sortGdrive/issues).

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information.

---

## 📬 Contact

Project Link: [https://github.com/Alprisz10/sortGdrive](https://github.com/Alprisz10/sortGdrive)

---

## 🙏 Credits

- **Nawa Alsaprise (Alprisz)** - Creator and Developer
- **rclone** - Excellent cloud sync tool ([https://rclone.org/](https://rclone.org/))

---

<p align="center">
  Made with ❤️ to bring order to digital chaos.
</p>
