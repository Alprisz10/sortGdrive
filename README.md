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

Tired of a messy cloud storage? **SortGdrive** is an intelligent, cross-platform Python script that automates the process of uploading and sorting your local files directly into neatly organized folders on Google Drive.

It acts as a smart bridge between your device and the cloud, scanning a specified folder and categorizing your files (like Images, Documents, Videos, and more) based on their extensions. No more manual folder creation or dragging and dropping!

---

## ✨ Key Features

*   **🌐 Truly Cross-Platform:** One codebase to rule them all. Works flawlessly on **Windows, Linux, macOS, and even Android (via Termux)**.
*   **🤖 Intelligent Auto-Categorization:** Automatically sorts files into custom folders (e.g., `Images`, `Documents`, `Archives`) in your Google Drive.
*   **🔌 Flexible Cloud Integration:** Supports direct connection via the robust **Google Drive API** or the powerful **`rclone`** tool for advanced syncing.
*   **⚙️ Highly Customizable:** Define your own folder structures and file extension rules through a simple, human-readable configuration file.
*   **🔒 Safe & Secure:** Uses official APIs and doesn't store your passwords. For the API method, you have full control over your credentials.

---

## 🗺️ How It Works: The Workflow

1.  **🔍 Scan:** The script begins by scanning the designated input source folder on your local device.
2.  **🏷️ Filter & Categorize:** It identifies each file's extension (e.g., `.pdf`, `.jpg`, `.mp4`) and maps it to a predefined category folder (e.g., `Documents`, `Images`, `Videos`).
3.  **☁️ Upload & Organize:** The files are then uploaded/moved to the corresponding, pre-created (or automatically created) folders within your Google Drive.

```
[Your Device Folder] --> [SortGdrive] --> [Google Drive]
     (Scan)              (Categorize)        (Organized)
          └── .pdf ──────────┐
          └── .jpg ─────┐    └──> 📁 Documents
          └── .mp4 ──┐  └────────> 📁 Images
                     └───────────> 📁 Videos
```

---

## 🚀 Step-by-Step Installation & Setup

Choose the guide that matches your operating system.

### 📋 Prerequisites
*   A **Google Cloud Platform (GCP) Project** with the Drive API enabled.
*   A downloaded `credentials.json` file from your GCP project. ([See Google's Guide](https://developers.google.com/drive/api/quickstart/python))

### 🪟 1. Windows Users

1.  **Install Python:** Download the latest version from [python.org](https://www.python.org/downloads/). **CRITICAL:** During installation, **check the box** that says **"Add Python to PATH"**.
2.  **Install Git:** Download and install [Git for Windows](https://git-scm.com/download/win). Use the default settings.
3.  **Open Terminal:** Press the `Windows` key, type **PowerShell**, and hit Enter.
4.  **Run these commands:**
    ```powershell
    git clone https://github.com/Alprisz10/sortGdrive
    cd sortGdrive
    pip install -r requirements.txt
    python main.py
    ```

### 🐧 2. Linux Users (Ubuntu/Debian)

Open your Terminal (`Ctrl+Alt+T`) and run:

1.  **Update & Install Tools:**
    ```bash
    sudo apt update && sudo apt upgrade -y
    sudo apt install git python3 python3-pip python3-venv -y
    ```
2.  **Clone & Run:**
    ```bash
    git clone https://github.com/Alprisz10/sortGdrive
    cd sortGdrive
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
    pip3 install -r requirements.txt
    python3 main.py
    ```
---

## ⚠️ Troubleshooting & Tips

### The "Externally Managed Environment" Error
If you see a red error about an "externally managed environment" when running `pip install`, your system is protecting the global Python installation. You **must** use a **Virtual Environment (venv)**:

**For Linux / macOS / Android:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

**For Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

### Using rclone as an Alternative
1.  Install `rclone` from [rclone.org](https://rclone.org/).
2.  Configure `rclone` to connect to your Google Drive (`rclone config`).
3.  Set `upload_method: "rclone"` in your `config.yaml`.
4.  Add your `rclone_remote_name: "your-remote-name"` to the config.

---

## 📁 Project Structure

```
sortGdrive/
├── Move_Dir             # default directory for file sorting container
├── main.py              # Main script to run
├── requirements.txt     # Python dependencies
├── README.md            # This file
└──  .gitignore           # Files to ignore in Git
```

---

## 🛣️ Roadmap / Future Ideas

- [ ] Add support for recursive folder scanning.
- [ ] Implement a GUI for easier configuration.
- [ ] Create a dry-run mode to preview changes without uploading.
- [ ] Add support for other cloud providers (Dropbox, OneDrive).

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

<p align="center">
  Made with ❤️ to bring order to digital chaos.
</p>
