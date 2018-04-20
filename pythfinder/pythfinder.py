""" Pythfinder.py

Main entry point for the pythfinder API

"""

import pythparser as Parser


def main(*args, **kwargs):
    args = Parser.ArgParser.parse()
    if Parser.ArgParser.process(args):
        print("Arguments parsed successfully")
    else:
        print("Bad Argument Occurred")


if __name__ == "__main__":
    main()
