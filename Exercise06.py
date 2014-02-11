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
testlist = testlist.split()

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


sorted_words = {}
for word in words:
    frequency = words[word]
    if sorted_words.get(frequency,False) == False:
        sorted_words[frequency] = [word]
    else:
        sorted_words[frequency].append(word)
        sorted_words[frequency].sort

for word in sorted(sorted_words, reverse = False):
    print str(word) + " "+ ', '.join(sorted_words[word])
    # print sorted_words[word]



twain.close()