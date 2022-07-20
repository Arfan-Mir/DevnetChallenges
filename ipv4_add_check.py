#
'''
This program validate the ipv4 address
Arfan Mir
Date July 20, 2022)
'''

while True:
    IPv4address = input('Enter IPv4 address to check if its valid (type x to end the program):')

    if IPv4address == 'x':
        print('Program ended')
        break
    parts = IPv4address.split('.')
    ipv4_add_check = True
    if len(parts) != 4:
        ipv4_add_check = False
    for part in parts:
        if not part.isnumeric():
            ipv4_add_check = False
            break
        if int(part) <= 0 or int(part) > 255:
            ipv4_add_check = False
            break
        if not isinstance(int(part), int):
            ipv4_add_check = False
    if ipv4_add_check:
        print("{} is a valid IPv4 address".format(IPv4address))
        print('')
    else:
        print("{} is not a valid IPv4 address".format(IPv4address))
        print('')
