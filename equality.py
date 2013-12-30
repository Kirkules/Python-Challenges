# The hint is "one small letter, surrounded by EXACTLY three big bodyguards on each of its sides

# There is an enormous block of characters in the source for the page, so use that.
# It's not yet clear whether the "big bodyguards" are supposed to be the same as each other,
# so at first I'm just going to search for a pattern of big-big-big-small-big-big-big.

# enormous block is stored in equality.txt
import re

if __name__ == "__main__":
    f = open("equality.txt","r+")
    theString = f.read()
    f.close()

    # match aAAAaAAAa, where the a's and A's can be any letter of like-capitalization
    # using regular expressions!!!
    pattern = "[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]"
    print("".join(re.findall(pattern,theString)))
