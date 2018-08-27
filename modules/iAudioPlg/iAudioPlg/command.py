#!/bin/env python
# -*- coding: utf8 -*-
import os
import re
import shutil


import wave
import struct
from scipy import *
from pylab import *

from pythong.project import write_setup_files
from pythong.util import ask_yes_no, read_config, write_config


def label(classifiers):
    """Takes a list of classifiers gathered by the
       project.prompt_classifiers() function and adds them to
       the setup.py file."""
    if os.path.isfile('.pythong'):
        try:
            config_data = read_config('.pythong')
            # TODO: fix dict so I can do config_data.project.classifiers,
            # so that I can add cool stuff to the config later that is
            # not about the project? dunno if necessary
            config_data['classifiers'] = classifiers
            write_config('.pythong', config_data)
            print "Modified .pythong config file with new classifiers."
            if ask_yes_no("Do you want to rebuild your setup.py from your new"
                          " config file? All manual changes will be erased.",
                           default=False):
                try:
                    write_setup_files(config_data['project_dir'])
                    print "Setup files written."
                except:
                    print "Problem writing setup files."
        except OSError:
            print "Can't open .pythong file in current directory."
    else:
        print "No .pythong file in current directory."


def pin(pin_list):
    """Add a list of files and directories to a MANIFEST.in
       file in the cwd."""
    # pin_list is a list inside of a list for some reason
    manifest = open('MANIFEST.in', 'a')
    for pin_item in pin_list[0]:
        if os.path.isfile(pin_item):
            manifest.write('include {}\n'.format(pin_item))
        elif os.path.isdir(pin_item):
            manifest.write('recursive-include {} *\n'.format(pin_item))
        else:
            pass # there is no file or dir with that name
    manifest.close()


def wash():
    """Remove all build/dist/egg-related files and .pyc files"""
    cwd = os.getcwd()
    delete_list = []
    for root, dirnames, filenames in os.walk(cwd):
        files_and_dirs = dirnames + filenames
        delete_list.extend([os.path.join(root, f) for f in files_and_dirs if \
                    re.search(r"\bbuild\b|\bdist\b|[^\s]*\.egg-info|.\.pyc",
                            f)])
    if len(delete_list) < 1:
        print "Your pythong is already sparkly-clean!"
    else:
        for f in delete_list:
            f_path = os.path.join(cwd, f)
            print "deleting {}".format(f_path)
            try:
                os.remove(f_path)
            except OSError:  # this means we've got a directory
                shutil.rmtree(f_path)
        print "Cleaned your pythong of {} files and directories.".format(
                len(delete_list))

def wavread():
 
	#读取wav文件，我这儿读了个自己用python写的音阶的wav
	filename = 'data/Noise.wav'
	wavefile = wave.open(filename, 'r') # open for writing

	#读取wav文件的四种信息的函数。期中numframes表示一共读取了几个frames，在后面要用到滴。
	nchannels = wavefile.getnchannels()
	sample_width = wavefile.getsampwidth()
	framerate = wavefile.getframerate()
	numframes = wavefile.getnframes()
	 
	print("channel",nchannels)
	print("sample_width",sample_width)
	print("framerate",framerate)
	print("numframes",numframes)
	 
	#建一个y的数列，用来保存后面读的每个frame的amplitude。
	y = zeros(numframes)
	 
	#for循环，readframe(1)每次读一个frame，取其前两位，是左声道的信息。右声道就是后两位啦。
	#unpack是struct里的一个函数，用法详见http://docs.python.org/library/struct.html。简单说来就是把＃packed的string转换成原来的数据，无论是什么样的数据都返回一个tuple。这里返回的是长度为一的一个
	#tuple，所以我们取它的第零位。
	for i in range(numframes):
	    val = wavefile.readframes(1)
	    left = val[0:2]
	#right = val[2:4]
	    v = struct.unpack('h', left )[0]
	    y[i] = v
	 
	#framerate就是44100，文件初读取的值。然后本程序最关键的一步！specgram！实在太简单了。。。
	Fs = framerate
	specgram(y, NFFT=1024, Fs=Fs, noverlap=900)
	show()

