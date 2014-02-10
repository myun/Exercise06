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

testlist = filetext
testlist = testlist.replace("--"," ")
testlist = filetext.split()

# for i in range(len(testlist)):
#     if testlist[i] != testlist[i].split("--"):
#         testlist.extend(testlist[i].split("--"))
#         del testlist[i]

for i in range(len(testlist)):
    testlist[i] = testlist[i].lower()
    testlist[i] = testlist[i].strip(',''.''!''--''"'';'':''_''?')
    if words.get(testlist[i],False) == False:
        words[testlist[i]] = 1
    else:
        words[testlist[i]] += 1

for word in words:
    print word + " " + str(words[word])

twain.close()