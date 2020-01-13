#!/usr/bin/env python
# encoding: utf-8


import argparse


parser = argparse.ArgumentParser()
parser.add_argument('x', type=int, help="the base")
args = parser.parse_args()
answer = args.x ** 2
print answer
