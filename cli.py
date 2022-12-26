from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from helper import save_cookie, load_cookie, save_cookie2
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from src import printcolors as pc
from src import artwork
import argparse
import click
import signal
import sys
import gnureadline

print("sample test case started")
driver = webdriver.Chrome()
driver.maximize_window()
# driver.get('https://www.varzesh3.com/')

# driver.get("https://class.kavano.org/class/you123/b4422df3")


def printlogo():
    pc.printout(artwork.ascii_art, pc.YELLOW)
    pc.printout("\nVersion 1.1 - Developed by Massooti\n\n", pc.YELLOW)
    pc.printout("Type 'list' to show all allowed commands\n")
    pc.printout(
        "Type 'FILE=y' to save results to files like '<target username>_<command>.txt (default is disabled)'\n")
    pc.printout("Type 'FILE=n' to disable saving to files'\n")
    pc.printout("Type 'JSON=y' to export results to a JSON files like '<target username>_<command>.json (default is "
                "disabled)'\n")
    pc.printout("Type 'JSON=n' to disable exporting to files'\n")


parser = argparse.ArgumentParser(description='Osintgram is a OSINT tool on Instagram. It offers an interactive shell '
                                 'to perform analysis on Instagram account of any users by its nickname ')
parser.add_argument(
    '-c', '--command', help='run in single command mode & execute provided command', action='store')

commands = {
    'banner':             printlogo, }

args = parser.parse_args()

if not args.command:
    printlogo()
# printlogo()


def signal_handler(sig, frame):
    pc.printout("\nGoodbye!\n", pc.RED)
    sys.exit(0)


def completer(text, state):
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None


def _quit():
    pc.printout("Goodbye!\n", pc.RED)
    sys.exit(0)


while True:
    if args.command:
        cmd = args.command
        _cmd = commands.get(args.command)
    else:
        signal.signal(signal.SIGINT, signal_handler)
        gnureadline.parse_and_bind("tab: complete")
        gnureadline.set_completer(completer)
        pc.printout("Run a command: ", pc.YELLOW)
        cmd = input()

        _cmd = commands.get(cmd)

    if _cmd:
        _cmd()
    elif cmd == "":
        print("")
    else:
        pc.printout("Unknown command\n", pc.RED)

    if args.command:
        break
