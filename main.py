meses = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"] # Lista com os meses do ano
chuva_mm = [] # Lista que vai armazenar os valores de chuva de cada mês
print("ANALISE DE CHUVA ANUAL")
print("-" * 30)
for mes in meses: # Percorre cada mês para coletar o valor de precipitação
    while True: # Repete até o usuário digitar um valor válido
        entrada = input(f"{mes}: ") # Solicita o valor de chuva do mês atual
        try:
            valor = float(entrada) # Tenta converter a entrada para número decimal
            if valor >= 0: # Aceita apenas valores não negativos
                chuva_mm.append(valor) # Adiciona o valor à lista
                break # Valor válido, passa para o próximo mês
            else:
                print("Valor deve ser >= 0") # Rejeita números negativos
        except:
            print("Digite um numero valido") # Rejeita entradas que não são números
total = 0
for v in chuva_mm:
    total = total + v # Acumula a soma de todos os meses
media = total / 12 # Calcula a média mensal
maior = chuva_mm[0] # Inicializa o maior valor com o primeiro mês
mes_maior = 0 # Índice do mês mais chuvoso
menor = chuva_mm[0] # Inicializa o menor valor com o primeiro mês
mes_menor = 0 # Índice do mês mais seco
for i in range(12):
    if chuva_mm[i] > maior: # Verifica se encontrou um mês mais chuvoso
        maior = chuva_mm[i]
        mes_maior = i
    if chuva_mm[i] < menor: # Verifica se encontrou um mês mais seco
        menor = chuva_mm[i]
        mes_menor = i
acima = 0
for v in chuva_mm:
    if v > media:
        acima = acima + 1 # Conta os meses acima da média
print("\nRESULTADOS:")
print("-" * 30)
print(f"Total anual:   {total:.0f} mm")
print(f"Media mensal:  {media:.1f} mm")
print(f"Mais chuvoso:  {meses[mes_maior]} ({maior:.0f} mm)")
print(f"Mais seco:     {meses[mes_menor]} ({menor:.0f} mm)")
print(f"Amplitude:     {maior - menor:.0f} mm")
print(f"Meses > media: {acima}/12")
print("\nGRAFICO:")
print("-" * 40)
for i in range(12):
    barras = int((chuva_mm[i] / maior) * 25) # Tamanho da barra proporcional ao maior valor
    print(f"{meses[i]} |{'#' * barras:<25}| {chuva_mm[i]:.0f}mm") # Exibe a barra do mês
print("-" * 40)
