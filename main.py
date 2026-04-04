import os
import sys
from datetime import datetime

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def titulo():
    """Exibe título formatado"""
    limpar_tela()
    print("=" * 60)
    print("🌧️  ANÁLISE COMPLETA DE CHUVA ANUAL 🌧️")
    print("=" * 60)
    print()

def menu():
    """Menu principal"""
    print("1️⃣  Análise com dados EXEMPLO (rápido)")
    print("2️⃣  Inserir dados PRÓPRIOS (interativo)")
    print("3️⃣  Sair")
    print("-" * 40)

def analise_chuva(chuva_mm, modo="exemplo"):
    """Função principal de análise"""
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
             "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    
    print("📊 DADOS DE CHUVA POR MÊS:")
    print("-" * 40)
    for i in range(12):
        print(f"{meses[i]:3s}: {chuva_mm[i]:6.0f} mm")
    
    # Cálculos
    total_anual = sum(chuva_mm)
    media_anual = total_anual / 12
    
    print("\n" + "="*50)
    print("📈 RESULTADOS DA ANÁLISE:")
    print("="*50)
    
    # 2. Média anual
    print(f"💧 Média anual:        {media_anual:7.1f} mm")
    
    # 3. Mês mais chuvoso
    idx_max = chuva_mm.index(max(chuva_mm))
    print(f"🌧️  Mais chuvoso:     {meses[idx_max]:3s} ({max(chuva_mm):4.0f} mm)")
    
    # 4. Mês mais seco
    idx_min = chuva_mm.index(min(chuva_mm))
    print(f"🌞 Mais seco:          {meses[idx_min]:3s} ({min(chuva_mm):4.0f} mm)")
    
    # 5. Meses acima da média
    acima_media = sum(1 for x in chuva_mm if x > media_anual)
    print(f"📊 Meses > média:      {acima_media:2d}/12 ({acima_media/12*100:5.1f}%)")
    
    print("\n" + "="*50)
    print("📋 RELATÓRIO COMPLETO:")
    print("="*50)
    print(f"• Total anual:     {total_anual:7.0f} mm")
    print(f"• Média mensal:    {media_anual:7.1f} mm")
    print(f"• Maior chuva:     {max(chuva_mm):7.0f} mm")
    print(f"• Menor chuva:     {min(chuva_mm):7.0f} mm")
    print(f"• Amplitude:       {max(chuva_mm)-min(chuva_mm):7.0f} mm")
    
    # Gráfico
    print("\n📊 GRÁFICO VISUAL (média = linha):")
    print("-" * 60)
    max_chuva = max(chuva_mm)
    linha_media = int((media_anual / max_chuva) * 30)
    
    for i in range(12):
        barras = int((chuva_mm[i] / max_chuva) * 30)
        status = "🔺" if chuva_mm[i] > media_anual else "🔻"
        linha_media_str = "─" * linha_media if i == 5 else ""
        print(f"{meses[i]:3s} |{ '█' * barras:<30} | {chuva_mm[i]:4.0f}mm {status} {linha_media_str}")
    
    print("-" * 60)
    print("─" * linha_media + "← Média")
    input("\nPressione ENTER para continuar...")

def modo_exemplo():
    """Dados de exemplo"""
    return [120, 80, 150, 90, 60, 200, 180, 110, 140, 95, 75, 130]

def modo_interativo():
    """Entrada de dados do usuário"""
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
             "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    chuva_mm = []
    
    print("📝 DIGITE OS DADOS DE CHUVA (mm):")
    print("(Pressione ENTER após cada valor)")
    
    for mes in meses:
        while True:
            try:
                valor = input(f"\n{mes}: ").strip()
                if valor.lower() == 'sair':
                    sys.exit("Programa encerrado.")
                valor = float(valor)
                if valor >= 0:
                    chuva_mm.append(valor)
                    break
                else:
                    print("❌ Valor deve ser >= 0")
            except ValueError:
                print("❌ Digite um número válido")
    
    return chuva_mm

def main():
    """Função principal"""
    while True:
        titulo()
        menu()
        
        opcao = input("\nEscolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            dados = modo_exemplo()
            analise_chuva(dados, "exemplo")
        elif opcao == "2":
            dados = modo_interativo()
            analise_chuva(dados, "interativo")
        elif opcao == "3":
            print("👋 Até logo!")
            break
        else:
            input("❌ Opção inválida! Pressione ENTER...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário!")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
