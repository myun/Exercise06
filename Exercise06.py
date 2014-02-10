#create an empty dictionary
#go through the file
#create a dictionary entry for every word
#increase the count for each word as we find it

# from sys import argv

# script, filename = argv

twain = open("twain.txt")
filetext = twain.read()

#teststring = "This is a string we are making to test things test things this This"
words = {}
print words
testlist = filetext.split()
for i in range(len(testlist)):
    testlist[i] = testlist[i].strip()
    if words.get(testlist[i],False) == False:
        words[testlist[i]] = 1
    else:
        words[testlist[i]] += 1

print words

twain.close()