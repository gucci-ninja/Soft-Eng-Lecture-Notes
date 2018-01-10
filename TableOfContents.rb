
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
    


