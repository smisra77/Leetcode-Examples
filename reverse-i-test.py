c = 'spam'

for i in range(len(c)):
    c = c[i:] + c[:i]
    print(c)

