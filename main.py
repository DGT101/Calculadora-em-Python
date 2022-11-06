from models import operacoes as op
from time import sleep


def main():

    print("--------CALCULADORA--------\n")
    print('/-/-/-/-/Operações/-/-/-/-/\n')

    sleep(2)

    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Resto da Divisão')
    print('6 - Raíz Quadrada')
    print('7 - Potenciação')
    print('8 - Sair do Programa')

    print('Digite a operação desejada: ')
    operacao = int(input())

    if operacao == 1:
        print('Digite os dois números que deseja somar: ')

        num1 = float(input())
        num2 = float(input())

        print('Resultado: ', op.soma(num1, num2))

        sleep(3)
        main()

    elif operacao == 2:
        print('Digite os dois números que deseja subtrair: ')

        num1 = float(input())
        num2 = float(input())

        print('Resultado: ', op.subtracao(num1, num2))

        sleep(3)
        main()

    elif operacao == 3:
        print('Digite os dois números que deseja multiplicar: ')

        num1 = float(input())
        num2 = float(input())

        print('Resultado: ', op.multiplicacao(num1, num2))

        sleep(3)
        main()

    elif operacao == 4:
        print('Digite os dois números que deseja dividir: ')

        num1 = float(input())
        num2 = float(input())

        print('Resultado: ', op.divisao(num1, num2))

        sleep(3)
        main()

    elif operacao == 5:
        print('Digite os dois números que deseja calcular o resto da divisão: ')
        print('OBS! O primeiro número é o dividendo, o segundo é o divisor')

        num1 = float(input())
        num2 = float(input())

        print('Resultado: ', op.resto_divisao(num1, num2))

        sleep(3)
        main()

    elif operacao == 6:
        print('Digite um número para calcular a raíz quadrada: ')

        num1 = float(input())

        print('Resultado: ', op.raiz_quadrada(num1))

        sleep(3)
        main()

    elif operacao == 7:
        print('Digite os dois números que deseja realizar a potenciação: ')
        print('OBS! O primeiro número é a base, o segundo número é o expoente')

        num1 = float(input())
        num2 = float(input())

        print('Resultado: ', op.potencia(num1, num2))

        sleep(3)
        main()

    elif operacao == 8:
        print('Programa finalizado!')

    else:
        print('Operação inválida!\n')

        sleep(3)
        main()


if __name__ == '__main__':
    main()
