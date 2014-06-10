CLS = '\033[2J'

NORMAL = '\033[0;37m\033[40m'
BOLD = '\033[1m'

class COLORS:
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    CYAN = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    YELLOW = '\033[0;36m'
    WHITE = '\033[0;37m'

    BOLD_BLACK = '\033[1;30m'
    BOLD_RED = '\033[1;31m'
    BOLD_GREEN = '\033[1;32m'
    BOLD_CYAN = '\033[1;33m'
    BOLD_BLUE = '\033[1;34m'
    BOLD_PURPLE = '\033[1;35m'
    BOLD_YELLOW = '\033[1;36m'
    BOLD_WHITE = '\033[1;37m'

    BLACK_BG = '\033[40m'
    RED_BG = '\033[41m'
    GREEN_BG = '\033[42m'
    CYAN_BG = '\033[43m'
    BLUE_BG = '\033[44m'
    PURPLE_BG = '\033[45m'
    YELLOW_BG = '\033[46m'
    WHITE_BG = '\033[47m'

def at(y, x):
    return '\033['+ str(y) +';'+ str(x) +'f'

def box(row, col, width, height):
    width = width - 2 # Subtract 2 for the left and right sides
    end = row + height-1
    print at(row, col) + u'\u2554' + u'\u2550'*width + u'\u2557'
    for i in range(row+1, end):
        print at(i, col) + u'\u2551' + " "*width + u'\u2551'
    print at(end, col) + u'\u255A' + u'\u2550'*width + u'\u255D'
