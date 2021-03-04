#Print uname and domain in this file

file = input("Enter a filename? ")

try:
    fh = open(file)
except:
    print("File not found!!!")
    quit()

db1 = list()

for line in fh:
    line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    db1.append(email)
#print(db1)
final_list = []

for e in db1:
    if e not in final_list:
        final_list.append(e)

print('All Emails: ', final_list)

for x in final_list:
#    print(db1)
    uname,domain = x.split('@')
    print('Uname:', uname, '\t\tDomain:', domain)







#    email = email.split('@')
 #   print(email)
#    uname,domain = email
#    print('Uname: ', uname, '\t\tDomain: ', domain)
#    for k, v in uname, domain:
#        db1.append((k,v))
#        uname, domain = e
#print(db1)

