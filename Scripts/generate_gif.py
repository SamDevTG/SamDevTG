import imageio
from datetime import datetime
from zoneinfo import ZoneInfo

FONT_FILE_BITMAP = "./fonts/gohufont-uni-14.pil"
FONT_FILE_MONA = "./fonts/Inversionz.otf"

def main():
    t = gifos.Terminal(800, 500, 15, 15, FONT_FILE_BITMAP, 15)
    t.set_fps(15)
    t.set_prompt("\x1b[0;91mSam\x1b[0m@\x1b[0;93mZorinOs ~> \x1b[0m")

    # Clear frame for fetching script
    t.clear_frame()
    t.gen_text("Fetching script", 1)
    t.gen_typing_text(".....", 1)
    t.gen_text("\x1b[96m", 1, count=0)  # Buffer to be removed
    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)

    # Display fetched script
    t.gen_text("\x1b[93mFetched Script\x1b[0m", 1, count=5)

    # Generate prompt for new command
    t.gen_prompt(2)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mfetch.s", 2, contin=True)
    t.delete_row(2, prompt_col)
    t.gen_text("\x1b[92mfetch.sh\x1b[0m", 2, contin=True)
    t.gen_typing_text(" -u Sam", 2, contin=True)

    # Display personal information
    t.set_font(FONT_FILE_BITMAP)
    t.toggle_show_cursor(True)
    t.gen_text(f"\n\n\x1b[30;101mSam@GitHub\x1b[0m", 1)
    t.gen_text("\n--------------", 2)
    t.gen_text("\x1b[96mOS:     \x1b[93mZorinOs\x1b[0m", 4)
    t.gen_text("\x1b[96mHost:   \x1b[93mThe Earth \x1b[94m#60.14 AU\x1b[0m", 5)
    t.gen_text("\x1b[96mKernel: \x1b[93mInformation Technology/Computer Science \x1b[94m#IT/CS\x1b[0m", 6)

    # Calculate age
    birth_date = datetime(2005, 11, 5, tzinfo=ZoneInfo("Europe/Lisbon"))
    current_date = datetime.now(ZoneInfo("Europe/Lisbon"))
    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    t.gen_text(f"\x1b[96mUptime: \x1b[93m{age} years", 7)

    # Display contact information
    t.gen_text("\n\n\x1b[30;101mContact:\x1b[0m", 9)
    t.gen_text("\n--------------", 10)
    t.gen_text("\x1b[96mEmail:      \x1b[93msamanthafontianha@gmail.com", 12)
    t.gen_text("\x1b[96mDiscord:    \x1b[93msam_872", 13)

    t.save_frame("screenshot.png")
    images = [imageio.imread("screenshot.png") for _ in range(10)]
    imageio.mimsave("output.gif", images, fps=15)

if __name__ == "__main__":
    main()
