import argparse
from Commands import register,login
import os

print("Selamat Datang di BNMO!")

parser = argparse.ArgumentParser()

parser.add_argument('foldername', type=str)
args = parser.parse_args()
for (root,dirs,files) in os.walk(args.foldername, topdown=True):
    print (files)


FUNCTIONS = {"register" : register, "log in" : login}
parser.add_argument('command', choices=FUNCTIONS.keys())
args = parser.parse_args()
func = FUNCTIONS[args.command]
func()

