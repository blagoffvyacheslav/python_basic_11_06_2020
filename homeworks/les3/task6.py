def int_func(word):
    return str(word).capitalize()

line = input('Введите строку: ')
line = line.split(' ')
string = str()
for word in line:
    string+=int_func(word)+' '

print(string)

