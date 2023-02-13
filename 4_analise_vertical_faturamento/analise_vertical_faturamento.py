"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de 
representação que cada estado teve dentro do valor total mensal da distribuidora.
"""
# Resolução do teste

def main():
    fatura_dict = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    faturamento_total = sum(fatura_dict[x] for x in fatura_dict)

    list_estados = list(fatura_dict.keys())
    list_faturamentos = list(fatura_dict.values())

    for i in range(len(list_estados)):
        print(list_estados[i] + ': ' + str(round(list_faturamentos[i], 2)) + 
                ' | ' + str(round((list_faturamentos[i] / faturamento_total)*100, 2)) + '%')
    print('Total faturamento: ' + str(round(faturamento_total, 2)) +
                ' | ' + str(round((faturamento_total / faturamento_total)*100, 2)) + '%')

if __name__== "__main__":
  main()
