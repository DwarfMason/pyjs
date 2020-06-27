import argparse

class KeysParser:
    def __init__(self):
        key_parser = argparse.ArgumentParser()
        key_parser.add_argument("-i", "--info", help="Prints short information about programmer",
                                action="store_true")
        args = key_parser.parse_args()
        if args.info:
            print(args.info)
            print("Created by Dwarf Mason. https://github.com/dwarfmason")

