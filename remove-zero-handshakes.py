#!/usr/bin/env python3
import subprocess
from subprocess import STDOUT
import string
import os
import sys

'''
Aircrack-ng and timeout needed, to install:
> sudo apt install aircrack-ng coreutil
For macOS
> sudo port install aircrack-ng timeout
'''


def check():
    try:
        subprocess.check_output(('aircrack-ng --help'), shell=True)
        print("[+] aircrackonly: aircrack-ng found.")
    except subprocess.CalledProcessError as grepexc:
        #print("error code", grepexc.returncode, grepexc.output)
        print("[-] aircrack-ng is not installed!")
        exit(-1)

def test_handshake(filename):
    todelete = 0
    handshakeFound = 0

    result = subprocess.run(('yes 1 | aircrack-ng ' + filename + ' 2>/dev/null | grep "1 handshake" | awk \'{print $2}\''), shell=True, stdout=subprocess.PIPE)

    result = result.stdout.decode('utf-8').translate({ord(c): None for c in string.whitespace})
    if result:
        handshakeFound = 1
        print("[+] contains handshake")

    if handshakeFound == 0:
        result = subprocess.run(('yes 1 | aircrack-ng ' + filename + ' 2>/dev/null | grep "PMKID" | awk \'{print $2}\''), shell=True, stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8').translate({ord(c): None for c in string.whitespace})
        if result:
            print("[+] contains PMKID")
        else:
            todelete = 1

    if todelete == 1:
        os.remove(filename)
        print("[*] Removed uncrackable pcap " + filename)


if __name__ == "__main__":
    print("[*] Sorting out pcap files without handshake...")
    check()

    if len(sys.argv) != 2:
        print("[-] Usage: python3 aircrackonly.py /path/to/handshake/folder")
        exit(-1)

    directory_str = sys.argv[1]
    # TODO: check directory_str

    directory = os.fsencode(directory_str)
    for f in os.listdir(directory):
        filename = os.fsdecode(f)
        if filename.endswith(".pcap"):
            fullpath = os.path.join(directory_str, filename)
            print("[*] Checking {}".format(fullpath))
            test_handshake(fullpath)
            continue
        else:
            continue