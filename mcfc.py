#
#       MCFC - Minecraft Formatting Codes
#
#   Author:    WoidZero
#   License:   MIT
#   Version:   1.0.1
#   Date:      2022-24-08
#


import os
import sys

# Check is console platform equal win32 and execute "color" command.
if sys.platform.lower() == "win32": 
    os.system('color')


# ================================================================ #


black = '\033[30m'
dark_blue = '\033[34m'
dark_green = '\033[32m'
dark_aqua = '\033[36m'
dark_red = '\033[31m'
dark_purple = '\033[35m'
gold = '\033[33m'

gray = '\033[0;37;40m'
dark_gray = '\033[1;30;40m'
blue = '\033[1;34;40m'
green = '\033[1;32;40m'
aqua = '\u001b[36;1m'
red = '\u001b[31;1m'
light_purple = '\u001b[35;1m'
yellow = '\033[1;33;40m'
white = '\u001b[37m'

reset = '\u001b[0m'
underlined = '\033[2;37;40m'


# ================================================================ #


codes = {
    "&0": black,
    "&1": dark_blue,
    "&2": dark_green,
    "&3": dark_aqua,
    "&4": dark_red,
    "&5": dark_purple,
    "&6": gold,
    "&7": gray,
    "&8": dark_gray,
    "&9": blue,
    "&a": green,
    "&b": aqua,
    "&c": red,
    "&d": light_purple,
    "&e": yellow,
    "&f": white,
    "&r": reset,
    "&n": underlined
}


# ================================================================ #


# formatting string
def f_print(text: str) -> str:
    for code in codes:
        text = text.replace(code, codes[code])

    print(u'{0}'.format(text) + u'{0}'.format(reset))


# ================================================================ #


# colors information
def colors():
    f_print("&00 &11 &22 &33 &44 &55 &66 &77 &88 &99\n &aa &bb &cc &dd &ee &ff &rr &nn")

f_print("&cSomething Red, &eSomething Yellow, &cR&eA&aI&bN&9B&dO&5W")


# ================================================================ #
