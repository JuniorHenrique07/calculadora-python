while True:

    num1 = int(input('Digite o Primeiro Número:'))
    num2 = int(input('Digite o Segundo Número:'))

    operacao = input('Selecione a operação (+, -, *, /): ') .strip()

    match operacao:

        case '+':
            res = num1+num2

        case '-':
            res = num1-num2

        case '*':
            res = num1*num2

        case '/':
            if num2 != 0:  
                res = num1/num2
            else:
                res = "Erro: Divisão por 0"  

        case _:
                res = "operacao invalida"     


    print    (f"Resultado é igual a: {res}")  

    rep = input("Deseja fazer outra operação? S/N:") .strip().lower()

    if rep != 's':
        print ('Calculadora Encerrada')
    