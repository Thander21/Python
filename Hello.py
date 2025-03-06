import os

# print("A","L","U","R","A",sep="\n")
# print(f"O valor arredondado de pi é: {pi:.2f}")


def exibir_nome():
    print("""
尺🝗丂七闩ㄩ尺闩𝓝セ🝗 ᗪㄖ 乙🝗́
    """)

def exibir_menu():
    print("1 - Cadastar")
    print("2 - Listar")
    print("3 - Ativar")
    print("4 - Sair")
    print()
    
    escolher_Opcoes()

def finalizar_app():
    os.system("cls")
    print("Obrigado por usar o nosso app\n")

def escolher_Opcoes():
    opcao_escolhida = int(input("Escolha uma opção: "))
    
    if opcao_escolhida == 1: 
        print("Cadastrar restaurante")
    elif opcao_escolhida == 2: 
        print("Listar restaurantes")
    elif opcao_escolhida == 3: 
        print("Ativar restaurante")
    elif opcao_escolhida == 4:
        finalizar_app()
    else: 
        os.system("cls")
        print("Opção inválida, escolha novamente:\n")
        exibir_menu()

def main():
    exibir_nome()
    exibir_menu()

if __name__ == "__main__":
    main()
