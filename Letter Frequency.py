#Letter frequency is simply the amount of times letters of the alphabet appear on average in written language
#https://en.wikipedia.org/wiki/Letter_frequency
import string

fname = 'romeo.txt'
d = dict()
l1 = list()

try:
    fh = open(fname)
except:
    print('Error reading file')
    quit()

for line in fh:
    line = line.rstrip()
    # maketrans(str1, str2, str3): str1 - characters need to be replaced, str2: replaced with what, str3: character to be deleted
    # translate(table): table - translate mapping specified to perform translations.
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
#        print('word: ', words)
        for letter in word:
#            print('letter: ', letter)
            d[letter] = d.get(letter, 0) + 1

print('Dictionery', d)

for k, v in list(d.items()):
    l1.append((v, k))

print('list', l1)

l1.sort(reverse = True)

print('Reversed list', l1)