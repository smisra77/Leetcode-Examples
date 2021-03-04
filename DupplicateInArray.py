#Find duplicate in array

array = [1, 34, 32, 34, 45, 12, 67, 45, 67, 34]
data = dict()
out = list()

l = len(array)

for x in array:
    data[x] = data.get(x, 0) + 1

print('Dictionary: ', data)

for k, v in data.items():
    if(v >= 2):
        out.append(k)

print('List: ', out)