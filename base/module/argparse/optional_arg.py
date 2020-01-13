#!/usr/bin/env python
# encoding: utf-8


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help="increase output verbosity",action="store_true")
args = parser.parse_args()
if args.verbosity:
            print "verbosity turned on"
