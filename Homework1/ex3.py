import re

def wordset(fname):
    """Returns the set of words corresponding to the given file"""
    # Create regexp for character filtering
    regex = re.compile('[^A-Za-z]')
    # Your code here

    wordSet = set()

    with open(fname) as f:
         for line in f:
             lineLower = line.lower()
             stringList = lineLower.split()

             for word in stringList:
                 word = regex.sub('', word)
                 wordSet.add(word)

    return wordSet



def jaccard(fname1, fname2):
    """Calculate Jaccard index"""
    # Your code here - call wordset()
    wordSet1 = wordset(fname1)
    wordSet2 = wordset(fname2)
    intersetion = len(wordSet1.intersection(wordSet2))
    union = len(wordSet1.union(wordSet2))
    return intersetion/union


FNAME1 = "alice_ascii.txt"
FNAME2 = "glass_ascii.txt"
print("Jaccard  index  between", FNAME1 , "and", FNAME2 , jaccard(FNAME1 , FNAME2 ))