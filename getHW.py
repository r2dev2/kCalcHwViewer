from webbot import Browser
import subprocess

assignmentpattern = "/assignment/view"

def getCredentials():
    f = open("credentials.txt", 'r')
    a = f.readlines()
    f.close()
    a = [i[:-1] for i in a]
    return a[0], a[1]

def grep(searchstr, filename):
    results = []
    for line in open(filename):
        if searchstr in line:
            results.append(line)
    return results

# returns web object
def loginLoop(username, password):
    web = Browser()
    web.go_to("https://lynbrook.schoolloop.com/")
    web.type(f"{username}\t{password}")
    web.click("Login")
    return web

def getHTML(web):
    a = web.get_page_source()
    s = open("schoolloopSource.txt", "w+")
    s.write(a)
    s.close()

def getAssignments(assignmentpattern):
    unparsedassignments = grep(assignmentpattern, "schoolloopSource.txt")
    assignments = []
    for i in unparsedassignments:
        assigidx = i.find('>')
        newassignment = ''
        for j in range(assigidx+1, len(i)):
            if i[j] == '<':
                break
            newassignment += i[j]
        assignments.append(newassignment)
    return assignments

def main():
    username, password = getCredentials()
    w = loginLoop(username, password)
    getHTML(w)
    a = getAssignments(assignmentpattern)
    subprocess.call("pkill chrome", shell=True)
    subprocess.call("rm schoolloopSource.txt", shell=True)
    return a

if __name__ == "__main__":
    main()
