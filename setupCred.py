import getpass
import subprocess

subprocess.call("rm .credentials.txt &>/dev/null", shell = True)

uname = input("Schoolloop Username\n")
print()
password = getpass.getpass(prompt="Password\n")

f = open(".credentials.txt", "w+")
f.write(uname + '\n' + password + '\n')
f.close()
