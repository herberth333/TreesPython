from models.Node import Node
import os

raiz = None

def mostrar_menu():
    print("\n" * 4)
    print("╔════════════════════════════════════╗")
    print("║    🌳 Projeto Herbert e Nabal 🌳  ║")
    print("╠════════════════════════════════════╣")
    print("║ 1. 🌱 Adicionar raiz da árvore    ║")
    print("║ 2. ➕ Inserir valor na árvore     ║")
    print("║ 3. 🖼️ Mostrar árvore              ║")
    print("║ 4. 🔁 Visualizar In-Order         ║")
    print("║ 5. 🔁 Visualizar Pre-Order        ║")
    print("║ 6. 🔁 Visualizar Post-Order       ║")
    print("║ 0. ❌ Sair                        ║")
    print("╚════════════════════════════════════╝")

while True:
    mostrar_menu()
    inputUser = input("🌟 Escolha uma opção: ")

    if inputUser == "1":
        dataRoot = int(input("Digite o valor da raiz: "))
        raiz = Node(dataRoot)
        print(f"🌱 Raiz definida: {dataRoot}")

    elif inputUser == "2":
        if raiz is None:
            print("⚠️ Defina a raiz primeiro (opção 1).")
            continue
        qtd = int(input("Quantos valores deseja inserir? "))
        for i in range(qtd):
            valor = int(input(f"Digite o valor do filho {i + 1}: "))
            raiz.insert(valor)
        print("🌿 Valores inseridos com sucesso!")

    elif inputUser == "3":
        if raiz is None:
            print("⚠️ Defina a raiz primeiro (opção 1).")
            continue
        if os.path.exists("arvore_bst.png"):
            os.remove("arvore_bst.png")
        raiz.visualizar_arvore()

    elif inputUser == "4":
        if raiz is None:
            print("⚠️ Defina a raiz primeiro (opção 1).")
            continue
        if os.path.exists("inorder_percorrido.png"):
            os.remove("inorder_percorrido.png")
        raiz.visualizar_inorder()

    elif inputUser == "5":
        if raiz is None:
            print("⚠️ Defina a raiz primeiro (opção 1).")
            continue
        if os.path.exists("preorder_percorrido.png"):
            os.remove("preorder_percorrido.png")
        raiz.visualizar_preorder()

    elif inputUser == "6":
        if raiz is None:
            print("⚠️ Defina a raiz primeiro (opção 1).")
            continue
        if os.path.exists("postorder_percorrido.png"):
            os.remove("postorder_percorrido.png")
        raiz.visualizar_postorder()

    elif inputUser == "0":
        print("👋 Saindo do programa... Até logo!")
        break

    else:
        print("⚠️ Opção inválida. Tente novamente.")
