stdform = input('Enter a number in scientific notation: ')
# Type your code below
stdform = stdform.strip(' ')
stdform1 = stdform.replace('.','')
stdform2 = stdform1.replace('-','')
pos_ = stdform2.find('x')
pos = stdform2.find('^')
if not stdform2[:pos_].isdigit():
    print('Error converting to scientific E notation.')
elif not stdform2[pos+1:].isdigit():
    print('Error converting to scientific E notation.')
elif not stdform.count('.') < 2:
    print('Error converting to scientific E notation.')  
elif not stdform.count('x') < 2:
    print('Error converting to scientific E notation.')
elif not stdform.count('^') < 2:
    print('Error converting to scientific E notation.')
else:
    stdform1 = stdform.replace('x10^','E')
    string = f'This number in E notation is {stdform1}.'
    print(string)


