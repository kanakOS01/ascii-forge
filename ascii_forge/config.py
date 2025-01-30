from colorama import Fore, Back, Style, init

init(autoreset=True)

ASCII_CHARS = "@#%*=+-:,. "
COLOR_MAP = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE,
}