#!/usr/bin/env python
# encoding: utf-8


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print args.echo
