import re

def wordset(fname):
    """Returns the set of words corresponding to the given file"""
    # Create regexp for character filtering
    regex = re.compile("[^A-Za-z]")
    # Your code here

    wordSet = set()

    with open(fname) as f:
        for line in f:
            #each line in the file is made lowercase and
            #stripped of special characters. Then, each
            #word is added to a list
            line = line.lower()
            withoutSymbols = regex.sub(' ', line)
            stringList = withoutSymbols.split()

            for word in stringList:
                wordSet.add(word)

    return wordSet



def jaccard(fname1, fname2):
    """Calculate Jaccard index"""
    # Your code here - call wordset()

    wordSet1 = wordset(fname1)
    wordSet2 = wordset(fname2)
    #intestection is calculated from the .intersection method for sets
    intersetion = len(wordSet1.intersection(wordSet2))
    #union is calculated from the .union method for sets
    union = len(wordSet1.union(wordSet2))
    return intersetion/union


FNAME1 = "alice_ascii.txt"
FNAME2 = "glass_ascii.txt"
print("Jaccard  index  between", FNAME1 , "and", FNAME2 , jaccard(FNAME1 , FNAME2 ))