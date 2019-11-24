import subprocess
import getHW

def getAssignments():
    u = getHW.main()
    a = []
    for i in u:
        if '#' in i:
            a.append(i)
    return a

def flip(ostr):
    nlist = [ostr[len(ostr)-i-1] for i in range(len(ostr))]
    return ''.join(nlist)

def getHwNums():
    lua = getAssignments()
    print(f"Math assignments: {lua}")
    nums = []
    for i in lua:
        idx = i.find(')')
        fa = ''
        yeet = False
        for j in range(idx, -1, -1):
            if yeet:
                continue
            if i[j] == ' ':
                yeet = True
            fa += i[j]
        a = flip(fa).replace(' ','')[:-1]
        nums.append(a)
    return nums

def downloadFromK(hwnums):
    subprocess.call("wget http://rkorsunsky.weebly.com/apcalculusbc.html", shell=True)
    links = ["rkorsunsky.weebly.com" for i in hwnums]
    for count, i in enumerate(hwnums):
        if subprocess.call(f"cat apcalculusbc.html | grep -m1 '{i}'", shell = True) == 1:
            continue
        unparsed = subprocess.check_output(f"cat apcalculusbc.html | grep -m1 '{i}'", shell = True)
        unparsed = unparsed.decode()
        idx = unparsed.find("/upload")
        if idx == -1:
            continue
        la = ''
        yeet = False
        for j in range(idx, len(unparsed)):
            if yeet:
                continue
            if unparsed[j] == '"':
                yeet = True
                continue
            la += unparsed[j]
        links[count] += la
    print(links)
    subprocess.call("rm apcalculusbc.html", shell=True)


def main():
    n = getHwNums()
    downloadFromK(n)


if __name__ == "__main__":
    main()
