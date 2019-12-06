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

def findall(search, parent):
    idxes = [i for i, ch in enumerate(parent) if ch == search]
    return idxes

def getHwNums():
    lua = getAssignments()
    print(f"Math assignments: {lua}")
    nums = []
    for i in lua:
        idx = findall(')', i)
        for k in idx:
            fa = ''
            yeet = False
            for j in range(k, -1, -1):
                if yeet:
                    continue
                if i[j] == ' ':
                    yeet = True
                fa += i[j]
            a = flip(fa).replace(' ','')[:-1]
            nums.append(a)
        idx = i.find("Wkst")
        oidx = idx
        if idx == -1:
            continue
        else:
            idx -= 2
        space = False
        while not space:
            print(i[idx])
            if i[idx] == ' ':
                space = True
                continue
            idx -= 1
        print(i[oidx + 3])
        print(i[idx: oidx + 3])
        nums.append(i[idx: oidx + 3])
    print("NUMMMMMSSSS", nums)
    return nums

def downloadFromK(hwnums):
    subprocess.call("wget http://rkorsunsky.weebly.com/apcalculusbc.html", shell=True)
    links = ["rkorsunsky.weebly.com" for i in hwnums]
    for count, i in enumerate(hwnums):
        endidx = i.find("Wk")
        wksearch = i[:endidx-1] + "_wksht"
        print("WKKKKKKK", wksearch)
        noreghw = subprocess.call(f"cat apcalculusbc.html | grep -m1 'hw{i}'", shell=True) == 1
        nowkst = subprocess.call(f"cat apcalculusbc.html | grep -m1 '{wksearch}'", shell=True) == 1
        if noreghw and nowkst:
            print("CONTINUING", wksearch)
            continue
        if "W" not in i and not noreghw:
            unparsed = subprocess.check_output(f"cat apcalculusbc.html | grep -m1 'hw{i}'", shell = True)
        elif not nowkst:
            print("SEARRCHING", wksearch)
            unparsed = subprocess.check_output(f"cat apcalculusbc.html | grep -m1 '{wksearch}'", shell = True)
        else:
            continue
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
    links = [i for i in links if i != "rkorsunsky.weebly.com"]
    print("LINKS:", links)
    subprocess.call("rm apcalculusbc.html", shell = True)
    for i in links:
        subprocess.call(f"wget {i}", shell = True)
    subprocess.call("mv *.pdf HW/", shell=True)


def main():
    subprocess.call("rm HW/*.pdf", shell=True)
    n = getHwNums()
    downloadFromK(n)


if __name__ == "__main__":
    main()
