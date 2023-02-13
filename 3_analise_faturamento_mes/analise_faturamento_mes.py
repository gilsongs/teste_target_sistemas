"""
3) Dado um vetor que guarda o valor de faturamento diário de uma 
distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e 
feriados. Estes dias devem ser ignorados no cálculo da média;
"""
# Resolução do teste

import json

def main():
    with open("dados.json", encoding='utf-8') as dados_json:
        fatura_dict = json.load(dados_json)

    # print(faturamento)

    menor_faturamento_mes = 0
    maior_faturamento_mes = 0
    media_faturamento_mes = 0
    dia_menor_faturamento = 0
    dia_maior_faturamento = 0
    dias_faturamento_mes = 0
    total_faturamento_mes = 0   

    for i in fatura_dict:
        if int(i['valor']) > 0:
            total_faturamento_mes = total_faturamento_mes + i['valor']
            dias_faturamento_mes += 1

            if menor_faturamento_mes == 0 or menor_faturamento_mes > i['valor']:
                menor_faturamento_mes = i['valor']
                dia_menor_faturamento = i['dia']
            if maior_faturamento_mes == 0 or maior_faturamento_mes < i['valor']:
                maior_faturamento_mes = i['valor']
                dia_maior_faturamento = i['dia']

    print('O menor valor de faturamento ocorrido no dia ' + str(dia_menor_faturamento) +': ' + str(round(menor_faturamento_mes, 2)))
    print('O maior valor de faturamento ocorrido no dia ' + str(dia_maior_faturamento) +': ' + str(round(maior_faturamento_mes, 2)))
    print('Total de faturamento no mês: ' + str(round(total_faturamento_mes, 2)))
    print('Total de dias com faturamento no mes:' + str(dias_faturamento_mes))

    media_faturamento_mes = total_faturamento_mes / dias_faturamento_mes
    print('Média de faturamento no mes: ' + str(round(media_faturamento_mes, 2)))

    dias_mes_fatura_sup_media_mes = 0
    for i in fatura_dict:
        if i['valor'] > media_faturamento_mes:
            dias_mes_fatura_sup_media_mes += 1 

    print('Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ' + str(dias_mes_fatura_sup_media_mes))        

if __name__== "__main__":
  main()
