import mechanize
import subprocess

assignmentpattern = "/assignment/view"

def getCredentials():
    f = open(".credentials.txt", 'r')
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

# Credit to @lithomas1 for mechanize
def getHTML(username, password):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
    sign_in = br.open("http://lynbrook.schoolloop.com")
    br.select_form(name = "form")
    br["login_name"] = username
    br["password"] = password
    logged_in = br.submit()
    req = br.open("http://lynbrook.schoolloop.com")

    with open("schoolloopSource.txt", 'wb') as fout:
        fout.write(req.read())

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
    getHTML(username, password)
    a = getAssignments(assignmentpattern)
    subprocess.call("rm schoolloopSource.txt", shell=True)
    print(a)
    return a

if __name__ == "__main__":
    main()
