#!/bin/python


import subprocess


def main():
    hunterCommand = ["sudo", "dpkg", "--list", "'linux-image*'", "|", "awk", "'{", "if", "($1==\"ii\")", "print $2}'", "|",  "grep",  "-v", "`uname", "-r`"]


    print(subprocess.run(hunterCommand))

    #for line in system(hunterCommand):
     #   print(type(line))
        #if line is not linux-image-generic:
         #   purger(line)


def purger(header):
    purgerCommand = "sudo apt-get purge " + header
    system(purge)
    print("Purged " + header)

main()

