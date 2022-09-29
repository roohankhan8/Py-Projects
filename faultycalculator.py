num1 = int(input('Enter first number: '))
operator = input('Enter operator: ')
num2 = int(input('Enter first number: '))

# if num1==45 & num2 == 3 & operator=='multiply':
#     print(555)

if operator=='/':
    if num1==56 and num2 == 6:
        print(4)
    else:
        print(int(num1/num2))

if operator=='*':
    if num1==45 and num2 == 3:
        print(555)
    else:
        print(int(num1*num2))

if operator=='+':
    if num1==56 and num2 == 9:
        print(77)
    else:
        print(int(num1+num2))

if operator=='-':
    print(int(num1-num2))
