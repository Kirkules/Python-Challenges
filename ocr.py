import collections

# get the characters to work with
f = open("ocr.txt","r+")
str = f.read()
f.close()

# make a defaultdict to accumulate the values
theD = collections.defaultdict(int)

# accumulate the values
for character in str:
    theD[character]+=1

# make and sort a list of the values
theL = [(key,value) for key,value in theD.items()]
theL = sorted(theL, key = lambda x:x[1])

# filter by too-frequent occurrence (<50 is fairly arbitrary here)
result = "".join([letter if (value < 50 and letter is not '\n') else '' for letter,value in theD.items()])

print(result)

# now that it's apparent that I need to have them in the order in which they
# originally appeared, since they're all just letters, I can do...
result = "".join([letter for letter in str if letter.isalpha()])
print(result)
