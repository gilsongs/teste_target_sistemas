"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência 
ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""
# Resolução do teste

def main():
    palavra = str(input("Entre com uma palavra qualquer: "))

    inversao_palavra = palavra[::-1]
    
    print(inversao_palavra)

if __name__== "__main__":
  main()
