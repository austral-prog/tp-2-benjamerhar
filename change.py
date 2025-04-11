def change():
    expense = 23.75
    money = 100
    Vuelto = money - expense
    Pesos = int(vuelto)
    Cents = Vuelto - Pesos
    CENTS = int(Cents * 100)
    print(f'Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n\nVuelto\n\nPesos:\n{Pesos}\nCentavos:\n{CENTS}')

