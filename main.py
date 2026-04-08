meses = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
chuva_mm = []

print("ANALISE DE CHUVA ANUAL")
print("-" * 30)

for mes in meses:
    while True:
        entrada = input(f"{mes}: ")
        try:
            valor = float(entrada)
            if valor >= 0:
                chuva_mm.append(valor)
                break
            else:
                print("Valor deve ser >= 0")
        except:
            print("Digite um numero valido")

total = 0
for v in chuva_mm:
    total = total + v

media = total / 12

maior = chuva_mm[0]
mes_maior = 0
menor = chuva_mm[0]
mes_menor = 0

for i in range(12):
    if chuva_mm[i] > maior:
        maior = chuva_mm[i]
        mes_maior = i
    if chuva_mm[i] < menor:
        menor = chuva_mm[i]
        mes_menor = i

acima = 0
for v in chuva_mm:
    if v > media:
        acima = acima + 1

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
    barras = int((chuva_mm[i] / maior) * 25)
    print(f"{meses[i]} |{'#' * barras:<25}| {chuva_mm[i]:.0f}mm")
print("-" * 40)
