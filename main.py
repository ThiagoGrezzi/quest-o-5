# Função para calcular a quantidade de litros de combustível utilizada na viagem
def calcular_litros_combustivel(tempo, velocidade_media):
    # Calcular a distância percorrida
    distancia = tempo * velocidade_media

    # Calcular a quantidade de litros utilizada
    litros_usados = distancia / 12.0  # 12 Km por litro

    return distancia, litros_usados

# Função principal
def main():
    try:
        # Obter input do usuário para o tempo e a velocidade média
        tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
        velocidade_media = float(input("Digite a velocidade média do veículo (em Km/h): "))

        # Calcular a distância e a quantidade de litros utilizada
        distancia, litros_usados = calcular_litros_combustivel(tempo, velocidade_media)

        # Apresentar os resultados
        print("\nResultados da viagem:")
        print(f"Velocidade Média: {velocidade_media} Km/h")
        print(f"Tempo Gasto: {tempo} horas")
        print(f"Distância Percorrida: {distancia} Km")
        print(f"Quantidade de Litros Utilizada: {litros_usados:.2f} litros")

    except ValueError:
        print("Por favor, digite valores numéricos válidos.")

if __name__ == "__main__":
    main()

