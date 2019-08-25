import random
x = str(random.randint(1000,9999))
def cows_and_bulls():
    cow_counter = 0
    d = {}
    sd = {'c1' : 0, 'c2' : 0, 'c3' : 0, 'c4': 0}
    while cow_counter<4:
        bull_counter = 0
        cow_counter = 0
        num = input('enter a four digit number: ')
        if x[0] == num[0]:
            cow_counter += 1
            d['c1'] = 1
        else:
            d['c1'] = 0
        if x[1] == num[1]:
            cow_counter += 1
            d['c2'] = 1
        else:
            d['c2'] = 0
        if x[2] == num[2]:
            cow_counter += 1
            d['c3'] = 1
        else:
            d['c3'] = 0
        if x[3] == num[3]:
            cow_counter += 1
            d['c4'] = 1
        else:
            d['c4'] = 0
        if sd['c1'] == 1 and d['c1'] == 0:
            bull_counter += 1
        if sd['c2'] == 1 and d['c2'] == 0:
            bull_counter += 1
        if sd['c3'] == 1 and d['c3'] == 0:
            bull_counter += 1
        if sd['c4'] == 1 and d['c4'] == 0:
            bull_counter += 1
        sd['c1'] = d['c1']
        sd['c2'] = d['c2']
        sd['c3'] = d['c3']
        sd['c4'] = d['c4']
        print(f'You have {cow_counter} cows, and {bull_counter} bulls')
cows_and_bulls()