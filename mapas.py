# FAIXA ETÁRIA ('TP_FAIXA_ETARIA')
mapa_faixa_etaria = {
1: 'Menor de 17 anos',
2: '17 anos',
3: '18 anos',
4: '19 anos',
5: '20 anos',
6: '21 anos',
7: '22 anos',
8: '23 anos',
9: '24 anos',
10: '25 anos',
11:	'Entre 26 e 30 anos',
12:	'Entre 31 e 35 anos',
13:	'Entre 36 e 40 anos',
14:	'Entre 41 e 45 anos',
15:	'Entre 46 e 50 anos',
16:	'Entre 51 e 55 anos',
17:	'Entre 56 e 60 anos',
18:	'Entre 61 e 65 anos',
19:	'Entre 66 e 70 anos',
20:	'Maior de 70 anos'
}

# COR / RAÇA ('TP_COR_RACA')
mapa_cor_raca = {
0: 'Não declarado',
1: 'Branca',
2: 'Preta',
3: 'Parda',
4: 'Amarela',
5: 'Indígena',
6: 'Não dispõe da informação'
}
# TIPO DA ESCOLA ('TP_DEPENDENCIA_ADM_ESC')
mapa_tipo_da_escola = {
1: 'Federal',
2: 'Estadual',
3: 'Municipal',
4: 'Privada'
}
# LOCAL DA ESCOLA ('TP_LOCALIZACAO_ESC')
mapa_localizacao_escola = {
1:	'Urbana',
2:	'Rural'
}
# ESCOLARIDADE PAI ('Q001')
mapa_escolaridade_pai ={
'A': 'Nunca estudou',
'B': 'Não completou a 4ª série/5º ano do Ensino Fundamental',
'C': 'Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental',
'D': 'Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio',
'E': 'Completou o Ensino Médio, mas não completou a Faculdade',
'F': 'Completou a Faculdade, mas não completou a Pós-graduação',
'G': 'Completou a Pós-graduação',
'H': 'Não sei'
}
# ESCOLARIDADE MÃE ('Q002')
mapa_escolaridade_mae ={
'A': 'Nunca estudou',
'B': 'Não completou a 4ª série/5º ano do Ensino Fundamental',
'C': 'Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental',
'D': 'Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio',
'E': 'Completou o Ensino Médio, mas não completou a Faculdade',
'F': 'Completou a Faculdade, mas não completou a Pós-graduação',
'G': 'Completou a Pós-graduação',
'H': 'Não sei'
}
# RENDA MENSAL FAMILIAR ('renda_familiar','Q006')
mapa_renda_familiar = {
'A': 'Nenhuma Renda',
'B': 'Até R$ 1.320,00',
'C': 'De R$ 1.320,01 até R$ 1.980,00',
'D': 'De R$ 1.980,01 até R$ 2.640,00',
'E': 'De R$ 2.640,01 até R$ 3.300,00',
'F': 'De R$ 3.300,01 até R$ 3.960,00',
'G': 'De R$ 3.960,01 até R$ 5.280,00',
'H': 'De R$ 5.280,01 até R$ 6.600,00',
'I': 'De R$ 6.600,01 até R$ 7.920,00',
'J': 'De R$ 7.920,01 até R$ 9240,00',
'K': 'De R$ 9.240,01 até R$ 10.560,00',
'L': 'De R$ 10.560,01 até R$ 11.880,00',
'M': 'De R$ 11.880,01 até R$ 13.200,00',
'N': 'De R$ 13.200,01 até R$ 15.840,00',
'O': 'De R$ 15.840,01 até R$ 19.800,00',
'P': 'De R$ 19.800,01 até R$ 26.400,00',
'Q': 'Acima de R$ 26.400,00'
}
ordem_renda = ['Nenhuma Renda', 'Até R$ 1.320,00', 'De R$ 1.320,01 até R$ 1.980,00', 'De R$ 1.980,01 até R$ 2.640,00', 'De R$ 2.640,01 até R$ 3.300,00', 'De R$ 3.300,01 até R$ 3.960,00', 'De R$ 3.960,01 até R$ 5.280,00', 'De R$ 5.280,01 até R$ 6.600,00', 'De R$ 6.600,01 até R$ 7.920,00', 'De R$ 7.920,01 até R$ 9240,00', 'De R$ 9.240,01 até R$ 10.560,00', 'De R$ 10.560,01 até R$ 11.880,00', 'De R$ 11.880,01 até R$ 13.200,00', 'De R$ 13.200,01 até R$ 15.840,00', 'De R$ 15.840,01 até R$ 19.800,00', 'De R$ 19.800,01 até R$ 26.400,00', 'Acima de R$ 26.400,00']

ordem_escolaridade_pais = ['Nunca estudou', 
'Não completou a 4ª série/5º ano do Ensino Fundamental',
'Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental',
'Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio',
'Completou o Ensino Médio, mas não completou a Faculdade',
'Completou a Faculdade, mas não completou a Pós-graduação',
'Completou a Pós-graduação',
'Não sei']

mapa_ponto_medio_renda_familiar = {
'Nenhuma Renda': 0,
'Até R$ 1.320,00' : (0 + 1320)/2,
'De R$ 1.320,01 até R$ 1.980,00': (1320 + 1980)/2,
'De R$ 1.980,01 até R$ 2.640,00': (1980 + 2640)/2,
'De R$ 2.640,01 até R$ 3.300,00': (2640 + 3300)/2,
'De R$ 3.300,01 até R$ 3.960,00': (3300 + 3960)/2,
'De R$ 3.960,01 até R$ 5.280,00': (3960 + 5280)/2,
'De R$ 5.280,01 até R$ 6.600,00': (5280 + 6600)/2,
'De R$ 6.600,01 até R$ 7.920,00': (6600 + 7920)/2,
'De R$ 7.920,01 até R$ 9240,00': (7920 + 9240)/2,
'De R$ 9.240,01 até R$ 10.560,00': (9240 + 10560)/2,
'De R$ 10.560,01 até R$ 11.880,00': (10560 + 11880)/2,
'De R$ 11.880,01 até R$ 13.200,00': (11880 + 13200)/2,
'De R$ 13.200,01 até R$ 15.840,00': (13200 + 15840)/2,
'De R$ 15.840,01 até R$ 19.800,00': (15840 + 19800)/2,
'De R$ 19.800,01 até R$ 26.400,00': (19800 + 26400)/2,
'Acima de R$ 26.400,00': 26400
}
