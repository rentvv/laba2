a = input()
if len(a)<6:
    print( 'пароль  короткий')
elif len(a) >6:
    b=input()
    if a==b:
        print('пароли совпадают')
    else:
        print('пароли не совпадают')