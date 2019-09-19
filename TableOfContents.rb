
# Local vars --- x = 9
# instance var (of object) --- @Counter
# Global vars --- $-x OR $name
# const --- starts with uppercase letter (Pi)
# .length of strings, arrays

def tocify(filename)
    # define table of contents
    toc = "## Table of Contents\n"

    # open the file
    f = File.open(filename, 'r')
    # store the first line
    first_line = f.readline()
    # this will tell us how long the table of contents originally was
    iTOC = 2

    # loops until there are no more lines to be read
    until f.eof()
        # read line
        line = f.readline().tr("\n", "")
        # check for existing table of contents and count how long it is
        if line["Table of Contents"]
            iTOC += 1
            line = f.readline()
            while line["-"] do
                iTOC += 1
                line = f.readline()
            end
        end
        # look for headings to put in table of contents
        if line.count('#') == 3
            header = line[4..-1].tr("\n", "") #trim off the first characters
            temp = header.tr(" ", "-").downcase # replace spaces and make lowercase
            link = temp.tr("!?,.')(", "") # remove punctuation
            toc.concat("- ["+header+"](#"+link+")\n")
        end
    end

    # read again but this time to trim off existing TOC
    tempf = IO.readlines(filename)
    f = tempf[iTOC..-1]

    # write to existing file
    towrite = File.open(filename, "w")
    towrite.puts (first_line + "\n" + toc + f.join(""))
end


filenames = ["3B/2B03/", "3B/3A04/", "3B/3DX4/", "3B/3I03/", "3B/3S03/",
"3B/4A03/", "3B/1BA3/", "3A/3DB3/", "3A/3BB4/", "Summer/Fast.ai/", "Summer/Algorithms and Data Structures/",
"4A/3Y03/", "4A/4E03/", "4A/4HC3/", "4A/4AA4/"]

filenames.each do |fname|
    puts fname
    tocify(fname+"README.md")
end
    


