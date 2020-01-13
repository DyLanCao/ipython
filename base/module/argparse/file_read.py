
from __future__ import print_function
import argparse
import os

def wavFileRead(directory):
    if not os.path.isdir(directory):
        raise Exception("Input path not found!")

    #Fs,X = readAudioFile(directory)
    print(Fs)
    print(X)

def parse_arguments():
    parser = argparse.ArgumentParser(description="A demonstration script "
            "for CoolAudio library")

    tasks = parser.add_subparsers(
            title="subcommands", description="available tasks",
            dest="task", metavar="")

    dirMp3Wav = tasks.add_parser("read",
            help="read a wav file "
            "to .wav format")
    dirMp3Wav.add_argument("-i", "--input", required=True, help="Input folder")
    dirMp3Wav.add_argument("-r", "--rate", type=int,
            choices=[8000, 16000, 32000, 44100], required=True,
            help="Samplerate of generated WAV files")
    dirMp3Wav.add_argument("-c", "--channels", type=int, choices=[1, 2],
            required=True,
            help="Audio channels of generated WAV files")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()


    if args.task == "read":
        # Convert fs for a list of wavs stored in a folder
        wavFileRead(args.input)
        print("args.rate:%d args.channels:%d " %(args.rate,args.channels))
        print(args.input)


