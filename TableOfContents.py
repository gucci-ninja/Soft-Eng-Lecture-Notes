# Script that goes through my lecture notes repo to find
# README.md files and creates a Table of Conects for each of them

    
def tocify(filename):
    toc = "## Table of Contents\n"
    with open(filename, "r", encoding="utf8") as f:
        first_line  = f.readline()
        endTOC = 2 # index at which current table of contents ends
        for line in f:
            if "Table of Contents" in line:
                endTOC += 1
                while("-" in f.readline()):
                    endTOC += 1                    
            if line.count('#') == 3 :
                header = line[4:].rstrip()
                temp = header.lower().replace(" ", "-")
                link = "".join(c for c in temp if c not in ('!', ',', '?', '.'))
                toc += ("- ["+header+"](#"+link+")\n")
    with open(filename, "r", encoding="utf8") as f:
        f = f.readlines()[endTOC:]
    with open(filename, 'w', encoding="utf8") as new:
        new.write(first_line + "\n" + toc + "".join(f))
                
filenames = ["3B/2B03/", "3B/3A04/", "3B/3DX4/", "3B/3I03/", "3B/3S03/",
             "3B/4A03/", "3A/3DB3/", "3A/3BB4/"]

for filename in filenames:
    print(filename)
    tocify(filename+"README.md")
