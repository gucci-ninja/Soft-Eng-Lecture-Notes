
# Method syntax
# def name(parameters)
#
# end
    # Local vars --- x = 9
    # instance var (of object) --- @Counter
    # Global vars --- $-x OR $name
    # const --- starts with uppercase letter (Pi)
    # .length of strings, arrays


toc = "## Table of Contents\n"
    
filename = "3B/README.md"

f = File.open(filename, 'r')
first_line = f.readline()
iTOC = 2

until f.eof()
    line = f.readline().tr("\n", "")
    if line["Table of Contents"]
        iTOC += 1
        line = f.readline()
        while line["##"] do
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
end

tempf = IO.readlines(filename)

puts iTOC

f = tempf[iTOC..-1]

towrite = File.open(filename, "w")

towrite.puts (first_line + "\n" + toc + f.join(""))

    




    


