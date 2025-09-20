import os
import shutil
import webbrowser
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Text Logo
logo = f"""
{Fore.RED}
   ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗
  ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝
  ██║     ██║     █████╗  ███████║██╔██╗ ██║███████╗
  ██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║╚════██║
  ╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████║
   ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
        {Fore.WHITE}Cleaner for Windows - CleanZa a Dolphin AI Product
"""

print(logo)

# Ask user which drive to clean
drive = input(Fore.RED + "\nEnter the drive letter to clean (e.g., C, D, E): ").upper()

if not drive or not os.path.exists(f"{drive}:\\"):
    print(Fore.RED + "Invalid drive! Exiting...")
    exit()

# Paths to clean
paths = [
    f"{drive}:\\Windows\\Temp",
    os.path.join(os.environ.get("TEMP", ""), ""),
    f"{drive}:\\Windows\\Prefetch",
    f"{drive}:\\Windows\\SoftwareDistribution\\Download",
    f"{drive}:\\$Recycle.Bin",
    f"{drive}:\\Windows\\Logs",
]

# Cleaning Process
def clean_path(path):
    if os.path.exists(path):
        try:
            shutil.rmtree(path, ignore_errors=True)
            os.makedirs(path, exist_ok=True)
            print(Fore.RED + f"[CLEANED] {path}")
        except Exception as e:
            print(Fore.RED + f"[FAILED] {path} -> {e}")

print(Fore.RED + "\nStarting cleaning process...\n")

for path in paths:
    clean_path(path)

# Delete Memory Dump File if exists
dump_file = f"{drive}:\\Windows\\MEMORY.DMP"
if os.path.exists(dump_file):
    try:
        os.remove(dump_file)
        print(Fore.RED + f"[CLEANED] {dump_file}")
    except Exception as e:
        print(Fore.RED + f"[FAILED] {dump_file} -> {e}")

print(Fore.RED + "\nCleaning Completed! ✅ Restart recommended.\n")

# Open YouTube video after cleaning
yt_link = "https://youtube.com/shorts/H0se-qAJARM?si=D5uanj7Vg2foOumd"
webbrowser.open(yt_link)

input(Fore.WHITE + "\nPress Enter to exit...")
