import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
        )
    parser.add_argument('first_file', help='file1.json')
    parser.add_argument('second_file', help='file2.json')
    parser.add_argument('-f', '--format', help='set format of output', default='stylish')
    parser.print_help()

    json.load(open('С:\\Python\\python-project-50\\gendiff\\scripts\\file1.json'))
    json.load(open('С:\\Python\\python-project-50\\gendiff\\scripts\\file2.json'))

if __name__ == "__main__":    
    main()

