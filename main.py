while True:
    print ('Введите число a')
    a = float(input ())

    print ('Введите число b')
    b = float(input ())

    print ('Выбирите опирацию')
    print ('1 - (a + b), 2 - (a - b) ,3 - (a * b)  , 4 - (a : b)')

    d = float(input ())

    if d==1:
        print('a + b =',a+b)

    if d==2:
        print('a - b =',a-b)

    if d==3:
        print('a * b =',a*b)

    if d==4:
        print('a : b =',a/b)
        

    print('Хотите продолжить : 1 - да , 2 - нет ')
    i = float(input ()) 
    
    if  i>1:
        break
       



    

    