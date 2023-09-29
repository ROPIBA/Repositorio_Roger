import random as rd
def main():
    USD=4108
    EUR=4454
    CNY=563
    JPY=28
    PEN=1106
    def convercion():
        a=int(input('¿A que diviza desea pasar?:\n 1.USD \n 2.EUR \n 3.CNY \n 4.JPY \n 5.PEN \n Respuesta= '))#inicio de las preguntas ppls del programa
        b=int(input('¿Cuantos pesos colombianos desea cambiar?: '))# final de las preguntas ppls del programa
        if a==1:
            print(f'{b} COP a USD son {b//4108} USD y la comicion por la transacción es= {comicion()}')
        elif a==2:
            print(b'COP a EUR son',b//4454,'EUR y la comicion por la transacción es= {y}')
        elif a==3:
            print(b,'COP a CNY son',b//563,'CNY y la comicion por la transacción es= {y}')
        elif a==4:
            print(b,'COP a JPY son',b//28,'JPY y la comicion por la transacción es= {y}')
        elif a==5:
            print(b,'COP a PEN son',b//1106,'PEN y la comicion por la transacción es= {y}')
    
    def comicion():
        y=round(rd.uniform(0.1,0.5),2)
        return y
    
    def tasas_comicion():
        Tusd= "a"
    
    def tasas():
        print(f'USD= {tasas_comicion()}COP\nEUR= EUR COP\nCNY= CNY COP\nJPY= JPY,COP\nPEN= PEN,COP')
        


    def menu(rta): #inicio del menú
        if rta==1:
            convercion() 
        elif rta==2:
            tasas()
        else:
            print('selección invalida')
        
    menu(int(input('¿Que desea hacer?: \n 1. Converción de  COP a otras divisas\n 2. Ver las tasas de cambio y su comición\n Respuesta= '))) #final del menú





if __name__=='__main__':
    main()