import imageio
from datetime import datetime
from zoneinfo import ZoneInfo
import os

FONT_FILE_BITMAP = "./fonts/gohufont-uni-14.pil"
FONT_FILE_MONA = "./fonts/Inversionz.otf"

def main():
    # Clear frame for fetching script
    os.system("clear")
    print("Fetching script")
    print(".....")

    # Display personal information
    print("\n\n\033[30;101mSam@GitHub\033[0m")
    print("--------------")
    print("\033[96mOS:     \033[93mZorinOs\033[0m")
    print("\033[96mHost:   \033[93mThe Earth \033[94m#60.14 AU\033[0m")
    print("\033[96mKernel: \033[93mInformation Technology/Computer Science \033[94m#IT/CS\033[0m")

    # Calculate age
    birth_date = datetime(2005, 11, 5, tzinfo=ZoneInfo("Europe/Lisbon"))
    current_date = datetime.now(ZoneInfo("Europe/Lisbon"))
    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    print(f"\033[96mUptime: \033[93m{age} years")

    # Display contact information
    print("\n\n\033[30;101mContact:\033[0m")
    print("--------------")
    print("\033[96mEmail:      \033[93msamanthafontianha@gmail.com")
    print("\033[96mDiscord:    \033[93msam_872")

    # Generate gif from terminal output
    os.system("convert -delay 100 -loop 0 -density 150 screenshot.png output.gif")

if __name__ == "__main__":
    main()
