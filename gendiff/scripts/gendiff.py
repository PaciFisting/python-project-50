import argparse


def main():
    parser = argparse.ArgumentParser(prog='gendiff')
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help=None)
    parser.add_argument('second_file', help=None)
    parser.print_help()

if __name__ == "__main__":    
    main()