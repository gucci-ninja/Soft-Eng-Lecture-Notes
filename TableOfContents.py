# Script that goes through my lecture notes repo to find
# README.md files and creates a Table of Conects for each of them

filenames = ["3B/2B03/", "3B/3A04/", "3B/3DX4/", "3B/3I03/", "3B/3S03/",
             "3B/4A03/", "3A/3DB3/", "3A/3BB4/"]

for filename in filenames:
    tocify(filename+"README.md")
    
def tocify(filename):
    toc = "## Table of Contents\n"
    
    with open(filename, "r") as f:
        first_line  = f.readline()
        for line in f:
            if line.count('#') == 3 :
                header = line[4:].rstrip()
                link = header.lower().replace(" ", "-")
                toc += ("- ["+header+"](#"+link+")\n")
    with open(filename, "r") as f:
        f = f.readlines()[1:]
    with open(filename, 'w') as new:
        new.write(first_line + "\n" + toc + "".join(f))
                
