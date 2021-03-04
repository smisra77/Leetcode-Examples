#Write a function that takes a string as input and reverse only the vowels of a string.
#Example 1: Given s = "hello", return "holle".
#Example 2: Given s = "leetcode", return "leotcede"

sent = "leetcode"
los = len(sent)
vow = []
index = []

def reversevowel(sent):
    for i in range(los):
        if sent[i] in ['a','e','i','o','u']:
            vow.append(sent[i])
            index.append(i)

    revvow = vow[::-1]
    print('Vowel List: ', revvow)
    print('Index List: ', index)

    result = []
    ind=0
    for i in range(los):
        if i in index:
            result.append(revvow[ind])
            ind += 1
        else:
            result.append(sent[i])

    print('Result List: ', result)
    return ''.join(result)

print(reversevowel(sent))



