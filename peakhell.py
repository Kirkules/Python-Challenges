# Kirk Boyer
# pythonchallenge.com challenges
# peakhell challenge

import pickle

# load the "banner" (which I renamed peakhell.p) as binary?
f = open("peakhell.p","rb")

b = pickle.load(f)

result = ""

for i in range(len(b)):
    for j in range(len(b[i])):
        for k in range(b[i][j][1]):
            result += b[i][j][0]
    result += "\n"

print(result)
