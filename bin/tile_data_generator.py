#!/usr/bin/python

import os
import getopt
import sys
import argparse

from tile_data_extractor.repositories import FileRepository
from tile_data_extractor.services import TileDataExtractionService
from tile_data_extractor.presenters import DataPresenterFactory

def main():
    parser = argparse.ArgumentParser(description='Extract tile information from PostgreSQL logs.')
    parser.add_argument('--input', dest='input_file', required=True,
                        help='input file to be parsed')
    parser.add_argument('--output', dest='output_file', required=True,
                        help='output file to be parsed')
    parser.add_argument('--format', dest='format', default='csv',
                        choices=['csv', 'json'], help='output format')

    args = parser.parse_args()
    run(args.input_file, args.output_file, args.format)


def run(input_file, output_file, format):
    repository = FileRepository(output_file)
    formater = DataPresenterFactory.build(format)
    service = TileDataExtractionService(repository, formater)
    service.process_file(input_file)

if __name__ == "__main__":
    main()
