import ctypes
import os
import platform
import subprocess
import sys
from subprocess import PIPE, STDOUT, Popen
from time import sleep

from halo import Halo

spinner = Halo(text='Please wait...', spinner='dots')


def main():
    """Main program"""
    portsToExpose = str(input('Ports to expose [Default: 22 for SSH]: '))
    print("Installing...\n")

    spinner.start()

    os.system("docker pull kalilinux/kali-rolling")

    if portsToExpose != "":
        os.system(
            f"docker run -dt --name kali-vm -p {portsToExpose}:{portsToExpose} -i kalilinux/kali-rolling")
    else:
        os.system(
            "docker run -dt --name kali-vm -p 22:22 -i kalilinux/kali-rolling")
        spinner.stop()
        os.system("docker exec -it kali-vm bash")


def run():
    """Program entry point"""
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        try:
            os._exit(1)
        except SystemExit:
            sys.exit(1)


if __name__ == "__main__":
    run()
