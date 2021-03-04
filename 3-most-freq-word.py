#3 most frequent words

para = "any of any any any any any a small set to of words or Affixes (such as a, an, and the) used with nouns to limit or give definiteness to the application. OR TO limit limit LIMIT to"


def three_words(p):
    words = p.lower().split()

# Get the set of unique words.
    uqs = []
    for word in words:
        if word not in uqs:
            uqs.append(word)
# Make a list of (count, unique) tuples.
    cts = []
    for uq in uqs:
        count = 0
        for word in words: # Iterate over the words.
            if word == uq:  # Is this word equal to the current unique?
                count += 1 # If so, increment the count
        cts.append((count, uq))

    cts.sort() # Sorting the list puts the lowest counts first
    cts.reverse()  # Reverse it, putting the highest counts first.
    #sorted(cts, reverse = True)
    print('cts', cts)

    for i in range(min(3, len(cts))):
        count, word = cts[i]
        print('%s %d' % (word, count))
    return

three_words(para)
