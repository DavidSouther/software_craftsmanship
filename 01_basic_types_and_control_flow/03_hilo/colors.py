CLEAR = '\033[2J'

NORMAL = '\033[0;37m'
BOLD = '\033[1m'

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
YELLOW = '\033[36m'
WHITE = '\033[37m'

BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_CYAN = '\033[43m'
BG_BLUE = '\033[44m'
BG_PURPLE = '\033[45m'
BG_YELLOW = '\033[46m'
BG_WHITE = '\033[47m'

BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_CYAN = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_PURPLE = '\033[95m'
BRIGHT_YELLOW = '\033[96m'
BRIGHT_WHITE = '\033[97m'

BRIGHT_BLACK_BG = '\033[100m'
BRIGHT_RED_BG = '\033[101m'
BRIGHT_GREEN_BG = '\033[102m'
BRIGHT_CYAN_BG = '\033[103m'
BRIGHT_BLUE_BG = '\033[104m'
BRIGHT_PURPLE_BG = '\033[105m'
BRIGHT_YELLOW_BG = '\033[106m'
BRIGHT_WHITE_BG = '\033[107m'

def at(y, x):
    return '\033['+ str(y) +';'+ str(x) +'f'

def box(row, col, width, height):
    width = width - 2
    end = row + height - 1
    print(at(row, col) + "\u2554" + "\u2550" * width + "\u2557")
    for i in range(row+1, end):
        print(at(i, col) + "\u2551" + " " * width + "\u2551")
    print(at(end, col) + "\u255A" + "\u2550" * width + "\u255D")
