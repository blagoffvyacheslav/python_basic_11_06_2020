digits = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('task4.txt', 'r') as file:
    with open('f2.txt', 'a') as file2:
        for l in file:
            for eng,rus in digits.items():
                if eng in l:
                    file2.write(l.replace(eng,rus))