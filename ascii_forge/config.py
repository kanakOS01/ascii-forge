from colorama import Fore, init

init(autoreset=True)

ASCII_CHARS = " .,:-+=*%#@"

COLOR_MAP = {
    "red": {"colorama": Fore.RED, "rgba": (255, 50, 50, 255)},
    "green": {"colorama": Fore.GREEN, "rgba": (50, 200, 50, 255)},
    "yellow": {"colorama": Fore.YELLOW, "rgba": (255, 230, 50, 255)},
    "blue": {"colorama": Fore.BLUE, "rgba": (50, 100, 255, 255)},
    "magenta": {"colorama": Fore.MAGENTA, "rgba": (200, 50, 200, 255)},
    "cyan": {"colorama": Fore.CYAN, "rgba": (50, 200, 255, 255)},
    "white": {"colorama": Fore.WHITE, "rgba": (230, 230, 230, 255)},
}

