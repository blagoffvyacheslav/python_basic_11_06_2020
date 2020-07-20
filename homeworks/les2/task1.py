l1 = []
l1.append(1)
l1.append(1.2)
l1.append(True)
l1.append({})
l1.append([])
l1.append(())
l1.append(set())
l1.append(frozenset())

for el in l1:
    print(type(el))