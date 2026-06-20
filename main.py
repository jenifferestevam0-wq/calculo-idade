def calcular_idade():
    nome = input("Digite seu nome completo: ")
    ano_atual = 2022
    
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            
            if 1922 <= ano_nascimento <= 2021:
                idade = ano_atual - ano_nascimento
                print(f"\nUsuário: {nome}")
                print(f"Idade em {ano_atual}: {idade} anos.")
                break
            else:
                print("Erro: O ano deve estar entre 1922 e 2021.")
        
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro para o ano.")

if __name__ == "__main__":
    calcular_idade()