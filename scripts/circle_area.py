#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calculate the area or the perimeter of a circle
"""

import argparse
import os

from my_research.utils.Circle import circle_area

def _build_arg_parser():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    p.add_argument('radius', type=float, metavar='RADIUS',
                   help='Radius of the circle.')
    return p

def main():
    parser = _build_arg_parser()
    args = parser.parse_args()

    aire = circle_area(args.rayon)
    print(f"L'aire du cercle de rayon {args.rayon} est : {aire:.2f}")

if __name__ == "__main__":
    main()
