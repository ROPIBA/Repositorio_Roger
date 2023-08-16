a = input("Ingrese una letra: ")

if a.isalpha() and len(a) == 1:
    if a in 'aeiou':
        print("Es vocal.")
    else:
        print("Es consonante.")
else:
    print("error, solo una letra.")
