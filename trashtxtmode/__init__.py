import os
import sys
import shlex
import struct
import platform
import subprocess

columns = 80
rows = 25


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'  # OK (In Blue)
    OKGREEN = '\033[92m'  # OK (In Green)
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # Reset Colors
    RESET = ENDC  # Alias for Reset Colors
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_terminal_size():
    """ getTerminalSize()
     - get width and height of console
     - works on linux,os x,windows,cygwin(windows)
     originally retrieved from:
     http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
    """
    current_os = platform.system()
    tuple_xy = None
    if current_os == 'Windows':
        tuple_xy = _get_terminal_size_windows()
        if tuple_xy is None:
            tuple_xy = _get_terminal_size_tput()
            # needed for window's python in cygwin's xterm!
    if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
        tuple_xy = _get_terminal_size_linux()
    if tuple_xy is None:
        print
        "default"
        tuple_xy = (80, 25)  # default value
    return tuple_xy


def _get_terminal_size_windows():
    try:
        from ctypes import windll, create_string_buffer
        # stdin handle is -10
        # stdout handle is -11
        # stderr handle is -12
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom,
             maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        pass


def _get_terminal_size_tput():
    # get terminal width
    # src: http://stackoverflow.com/questions/263890/how-do-i-find-the-width-height-of-a-terminal-window
    try:
        cols = int(subprocess.check_call(shlex.split('tput cols')))
        rows = int(subprocess.check_call(shlex.split('tput lines')))
        return (cols, rows)
    except:
        pass


def _get_terminal_size_linux():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            cr = struct.unpack('hh',
                               fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            return cr
        except:
            pass

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            return None
    return int(cr[1]), int(cr[0])


def cls():
    print("\n"*rows)


def termcls():
    try:
        os.system("cls")
    except OSError:
        try:
            os.system("clear")
        except OSError:
            pass


def allcls():
    try:
        os.system("cls")
    except OSError:
        try:
            os.system("clear")
        except OSError:
            cls()


def hline(thickness):
    if thickness == 0:
        print(" "*columns)
    elif thickness == 1:
        print("-"*columns)
    elif thickness == 2:
        print("="*columns)
    elif thickness == 3:
        print(":"*columns)
    elif thickness == 4:
        print("#"*columns)
    else:
        return Exception


def title(txt):
    print(colors.UNDERLINE+colors.BOLD+txt.upper()+colors.RESET)


def tryautosize():
    global rows
    global columns
    try:
        columns, rows = get_terminal_size()
        return True
    except:
        return False


def forceupdate():
    sys.stdout.flush()


def clearcurrentline():
    sys.stdout.write("\r")
    forceupdate()