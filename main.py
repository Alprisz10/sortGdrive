from rclone_python import rclone
from rclone_python.remote_types import RemoteTypes
import os, click, platform, sys
from colorama import Fore, Back, init

drive_name = "sortGdrive"
default_dir = "Move_dir"
folder_gdrive = ["Documents","Documents/Word_Processing","Documents/Spreadsheets","Documents/Presentation","Documents/Archives","Photos","Videos","Applications","Audios"]

grouping = {
  "Documents/Word_Processing": [".docx", ".doc", ".pdf", ".odt", ".rtf", ".txt"],
  "Documents/Spreadsheets": [".xlsx", ".xls", ".csv", ".ods"],
  "Documents/Presentation": [".pptx", ".ppt", ".odp"],
  "Documents/Archives": [".7z", ".zip", ".tar", ".tar.bz2", ".tar.gz", ".tar.xz", ".tar.lz4", ".tar.zstd", ".rar", ".zipx"],
  "Photos": [".jpg", ".jpeg", ".png", ".webp", ".raw", ".tiff", ".psd", ".heic", ".heif", ".gif", ".svg"],
  "Videos": [".mp4", ".mov", ".mkv", ".webm", ".flv", ".avi", ".wmv"],
  "Audios": [".mp3", ".aac", ".m4a", ".wav", ".flac", ".ogg", ".mid", ".midi", ".wma"],
  "Applications": [".msi", ".app", ".dmg", ".deb", ".rpm", ".bin", ".run", ".appimage", ".ipa", ".xapk", ".aab", ".iso", ".nspro", ".xci", ".vpk"]
}

init(autoreset = True)

def rcloneCheck():
    current_os = platform.system().lower()
    null_device = "NUL" if "windows" in current_os else "/dev/null"
    
    cek = os.system(f"rclone --version > {null_device} 2>&1")
    
    if cek != 0:
        print(f"{Fore.YELLOW}Rclone not found. Trying to install...")
        
        install_cmd = ""

        if "linux" in current_os or "android" in current_os:
            if os.path.exists("/data/data/com.termux"):
                install_cmd = "pkg install rclone -y"
            else:
                install_cmd = "sudo apt install rclone -y"
                
        elif "windows" in current_os:
            install_cmd = "winget install Rclone.Rclone"
            
        elif "darwin" in current_os:
            install_cmd = "brew install rclone"

        if install_cmd:
            print(f"{Fore.CYAN}Running: {install_cmd}")
            install_res = os.system(install_cmd)
            
            if install_res == 0:
                print(f"{Fore.GREEN}Rclone successfully installed!")
            else:
                print(f"{Fore.RED}Automatic installation failed. Try running '{install_cmd}' manually.")
                sys.exit()
        else:
            print(f"{Fore.RED}OS '{platform.system()}' not automatically supported.")
            sys.exit()

rcloneCheck()

def Logo():
  var_logo = ["╔══╗╔═╗╔═╗╔══╗  ╔══╗╔══╗╔═╗╔══╗╔╗─╔╗╔═╗","║══╣║║║║╬║╚╗╔╝  ║╔═╣╚╗╗║║╬║╚║║╝║╚╦╝║║╦╝","╠══║║║║║╗╣─║║─  ║╚╗║╔╩╝║║╗╣╔║║╗╚╗║╔╝║╩╗","╚══╝╚═╝╚╩╝─╚╝─  ╚══╝╚══╝╚╩╝╚══╝─╚═╝─╚═╝","──────────────  ───────────────────────","ᴍᴀᴅᴇ ʙʏ ɴᴀᴡᴀ ᴀʟsᴀᴘʀɪsᴇ (ᴀʟᴘʀɪsᴢ)","─────────────────────────────"]
  
  for frame in var_logo:
    print(f"{Fore.BLUE}{frame}")


def DirCheck():
  print(f"{Fore.YELLOW}Checking folders..")
  for folder in folder_gdrive:
    os.system(f"rclone mkdir {drive_name}:{folder}")
    
def sortirFile(folder_move):
  folder_move = os.path.expanduser(folder_move)
  folder_abs = os.path.abspath(folder_move)
  
  if not os.path.isdir(folder_abs):
        print(f"{Fore.RED}Error: Folder '{folder_move}' not found. Process cancelled.")
        input("press enter to go back")
        return
      
  file_count = 0
  for filename in os.listdir(folder_abs):
    path_lengkap = os.path.join(folder_abs, filename)
    if os.path.isdir(path_lengkap):
      continue
      
    name, ext = os.path.splitext(filename)
    ext = ext.lower()
    
    for kel, frmt in grouping.items():
      if ext in frmt:
        source_path = os.path.join(folder_abs, filename)
        source_path = source_path.replace(os.sep, '/')
        rclone.move(source_path, f"{drive_name}:{kel}")
        print(f"{Fore.GREEN}Moving: {filename} -> {kel}")
        file_count += 1
        break
    
  if file_count > 0:
    print(f"{Fore.GREEN}Total {file_count} files successfully moved ✓")
  else:
    print(f"{Fore.YELLOW}No files matched the grouping")

try:
  rclone.create_remote(drive_name, RemoteTypes.drive)
  print(f"{Fore.GREEN}Remote {drive_name} successfully created/exists")
except Exception as e:
  print(f"{Fore.YELLOW}Remote {drive_name} might already exist or error: {e}")

while True:
  try:
    click.clear()
    Logo()
    print(f"{Fore.WHITE}1. Reconfigure\n2. Sort files from default folder\n3. Sort files from custom folder")
    input_menu = int(input("enter your choice : "))
    
    if input_menu == 1:
      while True:
        input_delrem = (input(f"{Fore.GREEN}are you sure you want to reset the Google Drive connection (y/n) : "))
        if input_delrem == "y":
          os.system(f"rclone config delete {drive_name}")
          print("connection successfully deleted ✓")
          print(f"{Fore.YELLOW}creating new connection..")
          rclone.create_remote(drive_name, RemoteTypes.drive)
          print(f"{Fore.GREEN}connection successfully created ✓")
          input(f"press enter to go back")
          break
          
        elif input_delrem == "n":
          break
        else:
          print(f"{Fore.RED}Invalid choice! Enter 'y' or 'n'")
          input("press enter to continue...")
          click.clear()
          
    elif input_menu == 2:
      if not os.path.exists(default_dir):
        print(f"{Fore.RED}Error: Default folder '{default_dir}' not found!")
        print(f"{Fore.YELLOW}Create folder '{default_dir}' first or use menu 3 for custom folder")
        input("press enter to go back")
        continue
        
      print(f"{Fore.YELLOW}Looking at your files..")
      try:
        files = os.listdir(default_dir)
        if files:
          for f in files:
            print(f"  - {f}")
        else:
          print(f"{Fore.YELLOW}Folder is empty")
      except Exception as e:
        print(f"{Fore.RED}Error reading folder: {e}")
        input("press enter to go back")
        continue
        
      while True:
        input_movefile = input(f"{Fore.GREEN}do you want to sort everything to google drive (y/n) : ")
        if input_movefile == "y":
          DirCheck()
          sortirFile(default_dir)
          print("press enter to go back")
          input()
          break
        elif input_movefile == "n":
          break
        else:
          print(f"{Fore.RED}Invalid choice! Enter 'y' or 'n'")
          click.clear()
          
    elif input_menu == 3:
      print()
      print(f"../ to jump out of this script's folder\n{Back.YELLOW}{Fore.BLACK}example : ../../downloads/browsers")
      print(f"or you can use a more specific path\n{Back.YELLOW}{Fore.BLACK}example : ~/storage/downloads/browsers")
      if platform.system().lower() == "windows":
        print(f"{Fore.YELLOW}Note: On Windows, '~' might not work. Use full path like 'C:/Users/...'")
      
      input_dir = input(f"{Fore.GREEN}enter destination folder : ")
      
      expanded_dir = os.path.expanduser(input_dir)
      if not os.path.exists(expanded_dir):
        print(f"{Fore.RED}Error: Folder '{input_dir}' not found!")
        input("press enter to go back")
        continue
        
      DirCheck()
      sortirFile(input_dir)
      input("press enter to go back")
        
  except ValueError:
    print(f"{Fore.RED}Wrong input! Must be a number (1, 2, or 3)")
    input("press enter to continue...")
  except KeyboardInterrupt:
    print(f"\n{Fore.YELLOW}Program stopped by user")
    sys.exit(0)