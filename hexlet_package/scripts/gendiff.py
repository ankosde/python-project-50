#!/usr/bin/env python3
import json
import argparse
from hexlet_package.generate import generate_diff

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    rgs = parser.parse_args()
    with open('hexlet_package/file1.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    with open('hexlet_package/file2.json', 'r', encoding='utf-8') as f:
        file2 = json.load(f)
    generate_diff(file1, file2)



if __name__ == '__main__':
    main()
