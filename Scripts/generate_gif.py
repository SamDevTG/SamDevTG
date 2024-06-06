from datetime import datetime
from pytz import timezone
import gifos

FONT_FILE_LOGO = "./fonts/vtks-blocketo.regular.ttf"
FONT_FILE_BITMAP = "./fonts/gohufont-uni-14.pil"
FONT_FILE_TRUETYPE = "./fonts/IosevkaTermNerdFont-Bold.ttf"
FONT_FILE_MONA = "./fonts/Inversionz.otf"

# Alteração: Usar o fuso horário de Lisboa
lisbon_tz = timezone('Europe/Lisbon')

def main():
    t = gifos.Terminal(800, 500, 15, 15, FONT_FILE_BITMAP, 15)
    t.set_fps(15)
    t.set_prompt("\x1b[0;91mSam\x1b[0m@\x1b[0;93mGitHub ~> \x1b[0m")

    # Alteração: Definir a data de nascimento para 5 de novembro de 2005
    birth_date = datetime(2005, 11, 5)

    # Alteração: Calcular a idade
    today = datetime.now(lisbon_tz).date()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    # one God day is equal 1000 human year.
    copyright_year = datetime.now().date().year / (1000 * 365.25)
    t.gen_text("", 1, count=20)
    t.toggle_show_cursor(False)
    t.gen_text("OS Modular BIOS v1.0.25", 1)
    t.gen_text(f"Copyright (C) {copyright_year}, \x1b[31mGod Inc.\x1b[0m", 2)
    t.gen_text("\x1b[94mGitHub Profile ReadMe Terminal, Rev 1011\x1b[0m", 4)
    t.gen_text("Krypton(tm) CPU - 250Hz", 6)
    t.gen_text(
        "Press \x1b[94mDEL\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to cancel Memory Test",
        t.num_rows,
    )
    for i in range(0, 65653, 7168):  # 64K Memory
        t.delete_row(7)
        if i < 30000:
            t.gen_text(
                f"Memory Test: {i}", 7, count=2, contin=True
            )  # slow down upto a point
        else:
            t.gen_text(f"Memory Test: {i}", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 64KB OK", 7, count=10, contin=True)
    t.gen_text("", 11, count=10, contin=True)

    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)
    t.gen_text("\x1b[96m", 1, count=0, contin=True)  # buffer to be removed
    t.set_font(FONT_FILE_LOGO, 66)
    os_logo_text = "OS"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 3, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)

    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mOS v1.0.25 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("sam", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*********", 4, contin=True)
    t.toggle_show_cursor(False)
    t.gen_text(f"Last login: {today.strftime('%a %b %d %I:%M:%S %p %Z %Y')} on
    t.gen_text(f"Last login: {today.strftime('%a %b %d %I:%M:%S %p %Z %Y')} on tty1", 6)

    t.gen_prompt(7, count=5)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mclea", 7, contin=True)
    t.delete_row(7, prompt_col)  # simulate syntax highlighting
    t.gen_text("\x1b[92mclear\x1b[0m", 7, count=3, contin=True)

    ignore_repos = ["dotfiles", "0x61nas.github.io", "obsidian"]
    git_user_details = gifos.utils.fetch_github_stats("0x61nas", ignore_repos)
    
    t.clear_frame()
    top_languages = [lang[0] for lang in git_user_details.languages_sorted]
    user_details_lines = f"""
    \x1b[30;101mSam@GitHub\x1b[0m
    --------------
    \x1b[96mOS:     \x1b[93mArch Linux\x1b[0m
    \x1b[96mHost:   \x1b[93mThe Earth \x1b[94m#60.14 AU\x1b[0m
    \x1b[96mKernel: \x1b[93mInformation Technology/Computer Science \x1b[94m#IT/CS\x1b[0m
    \x1b[96mUptime: \x1b[93m{age} years old\x1b[0m
    \x1b[96mIDE:    \x1b[93mHelix\x1b[0m
    
    \x1b[30;101mContact:\x1b[0m
    --------------
    \x1b[96mEmail:      \x1b[93m0x61nas@gmail.com\x1b[0m
    \x1b[96mDiscord:    \x1b[93m@0x61nas\x1b[0m
    
    \x1b[30;101mGitHub Stats:\x1b[0m
    --------------
    \x1b[96mUser Rating: \x1b[93m{git_user_details.user_rank.level}\x1b[0m
    \x1b[96mTotal Stars Earned: \x1b[93m{git_user_details.total_stars}\x1b[0m
    \x1b[96mTop Languages: \x1b[93m{', '.join(top_languages)}\x1b[0m
    """

    t.gen_text(user_details_lines, 1)

    t.render()


if __name__ == "__main__":
    main()
