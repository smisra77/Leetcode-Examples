#Find word in file and count

word = raw_input("Enter a word: ")
infile = 'input-1.txt'

def word_count(w):
    count = 0
    with open(infile, 'r') as f:
        for w in f.readlines():
            count += 1
            #print(w)
        return count

c = word_count(word)
print ("Total count for word '%s' is: %d" % (word,c))
    
