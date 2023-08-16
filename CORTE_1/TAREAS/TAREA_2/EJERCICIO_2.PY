a=eval(input('ingrese el tiempo (en minutos) que usó en el parqueadero: '))
b=139*a #subtotal
c=b*0.19 #IVA
d=b+c #total
e=((d + 49) // 50) * 50 # arreglo para pago
print('Recibo de parqueadero\n''Tiempo:',a,' minutos' '\n' 'Subtotal: ',b, 'pesos' '\n' 'IVA: ',c, 'pesos' '\n' 'Total: ', e, 'pesos')

