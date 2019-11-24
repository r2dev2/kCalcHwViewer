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
        a = flip(fa).replace(' ','')
        nums.append(a)
    return nums

def downloadFromK(hwnums):
    print(nums)

def main():
    getHwNums()

if __name__ == "__main__":
    main()
