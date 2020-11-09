# -*- coding: UTF-8 -*-

def num_split(number_string="13 43 6 222 12 43 64 23"):
    list_of_numbers = [int(i) for i in number_string.split(" ")]
    even =[]
    uneven = []
    unknown= []
    for i in list_of_numbers:
        if i % 2 !=0:
            uneven.append(i)
        elif i % 2 == 0:
            even.append(i)
        else:
            unknown.append(i)
    print(even, uneven, unknown)
    return (even, uneven, unknown)

if __name__ == '__main__':
    usage = '%(prog)s'
    description = 'PhoolBox_description'
    num_split()
