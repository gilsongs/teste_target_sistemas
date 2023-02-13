"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o 
próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa 
na linguagem que desejar onde, informado um número, ele calcule a 
sequência de Fibonacci e retorne uma mensagem avisando se o número 
informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua 
preferência ou pode ser previamente definido no código;
"""
# Resolução do teste

def main():
    n = int(input("Informe o número para verificar na sequência Fibonacci: "))

    fibonacci = [0, 1]

    if (n==fibonacci[0]) or (n==fibonacci[1]):
        print('O valor ' + str(n) + ' pertence a sequência Fibonacci!' + str(fibonacci))
    else:
        anterior = 0
        proximo = 1
        i = 2

        while proximo < n:
            fibonacci.append(anterior + proximo)
            anterior = proximo
            proximo = fibonacci[i]
            i = i + 1

        try:
            indice = fibonacci.index(n)
        except ValueError:
            print('O valor ' + str(n) + ' não pertence a sequência Fibonacci!' + str(fibonacci))
        else:
            print('O valor ' + str(n) + ' pertence a sequência Fibonacci!' + str(fibonacci))

if __name__== "__main__":
  main()
