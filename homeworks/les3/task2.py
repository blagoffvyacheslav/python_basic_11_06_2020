name = input('Введите имя: ')
lastname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город рождения: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')
def person(name=name, lastname=lastname, year=year, city=city, email=email, phone=phone):
    print('Name: {}, lastname: {}, year: {}, city: {}, email: {}, phone: {}'.format(name, lastname, year, city, email, phone))

person(name, lastname, year, city, email, phone)