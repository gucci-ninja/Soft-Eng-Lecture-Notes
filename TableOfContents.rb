
# Method syntax
# def name(parameters)
#
# end
def tocify(filename)
    # Local vars --- x = 9
    # instance var (of object) --- @Counter
    # Global vars --- $-x OR $name
    # const --- starts with uppercase letter (Pi)
    # .length of strings, arrays

    toc = "## Table of Contents\n"

    # open file to read
    #f = File.open(filename, "r")
    f = IO.readlines(filename)
    first_line = f[0]

    # index 
    iTOC = 2

    # until end of file
    until f.eof()
        # Read line
        line = f.readline()
        if line.grep("Table of Contents")
            iTOC += 1
            line = f.readline()
            while line.grep("##") do
                iTOC += 1
                line = f.readline()
            end
        end
        if line.count('#') == 3
            header = line[4..-1].tr("\n", "")
            temp = header.tr(" ", "-").downcase
            link = temp.tr("!?,.", "")
            toc.concat("- ["+header+"](#"+link+")\n")
        end
    tempf = IO.readlines(filename)

    f = tempf[iTOC..-1]

    towrite = File.open(filename, "w")

    towrite.puts (first_line + "\n" + toc + f.join(""))

        


    


