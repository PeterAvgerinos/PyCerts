counts = { 'quincy' : 1, 'mrugesh' : 42, 'beau' : 100, '0' : 10}
print(counts)

lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse = True)
print(lst)

print(sorted([(v,k) for k,v in counts.keys()]))
