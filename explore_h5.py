import h5py
import argparse
import numpy as np


def print_node(node, indent: int = 4):
    """

    :param node:
    :param indent:
    :return:
    """
    *first, last = str(node).split("/")
    print(" " * indent * len(first), last)


def print_h5(h5filename, indent=4):
    """ For a given HDF5 file"""
    with h5py.File(h5filename, mode='r') as h5file:
        h5file.visit(lambda node: print_node(node, indent=indent))


def main():
    parser = argparse.ArgumentParser(description="HDF5 file to display")
    parser.add_argument('h5file')
    args = parser.parse_args()
    print(args.h5file)
    print_h5(args.h5file)


if __name__ == "__main__":
    main()
