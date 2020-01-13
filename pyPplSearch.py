#Opens BackgroundCheck.com

import webbrowser

while True:
    city = input('What city? ')
    state = input('What state? ')
    form = input("Is this a name, address, or phone? ")

    if form.lower() not in ('name', 'address', 'phone'):
        print("Invalid answer!")
    else:
        break

if form.lower() == 'name':
    person = '-'.join(input('Person: ').split(' '))

    webbrowser.open('http://www.smartbackgroundchecks.com/people/' + person + '/' + city + '/' + state)

elif form.lower() == 'address':
    place = '-'.join(input('Address: ').split(' '))
    
    webbrowser.open('http://www.smartbackgroundchecks.com/address/' + place + '/' + city + '/' + state)

elif form.lower() == 'phone':
    phone = input('Phone: ')

    webbrowser.open('http://www.smartbackgroundchecks.com/phone/' + phone)