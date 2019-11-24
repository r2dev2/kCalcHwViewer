import subprocess
import downloadK

def main():
    downloadK.main()
    subprocess.call("evince HW/*.pdf &>/dev/null", shell=True)

if __name__ == "__main__":
    main()
