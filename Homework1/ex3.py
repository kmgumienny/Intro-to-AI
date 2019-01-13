import re

def wordset(fname):
    """Returns the set of words corresponding to the given file"""
    # Create regexp for character filtering
    regex = re.compile('[^a-zA-Z ]')
    # Your code here

def jaccard(fname1, fname2):
    """Calculate Jaccard index"""
    # Your code here - call wordset()
