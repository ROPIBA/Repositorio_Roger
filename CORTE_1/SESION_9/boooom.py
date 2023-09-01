def cuenta_atras (num):
    print(num)
    num-=1
    if num>0:
        cuenta_atras(num)
    else:
        print('BOOOOM¡')
    print('fin de la funcion',num)







if __name__=="__main__":
    cuenta_atras(5)