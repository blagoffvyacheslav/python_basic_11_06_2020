l = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print ([el for idx, el in enumerate(l) if idx>0 and l[idx]>l[idx-1]])