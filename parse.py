import os, re, csv

regex = re.compile(r"\@([a-z0-9][a-z0-9._-]*)")
contributers = {}
fileCount = 0

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.lower().endswith(".txt"):
            fileCount+=1
            file = open(file, 'r')
            text = file.read()
            file.close()
            # name = regex.search(text)
            for (name) in re.findall(regex, text):
                if name in contributers:
                    contributers[name]+=1
                else:
                    contributers[name]=1

with open("people.csv", 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for person, count in contributers.items():
        wr.writerow([person, count])
print len(contributers)
print fileCount