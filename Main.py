from models.Node import Node
                    
# Exemplo de uso:
raiz = Node(8)
nosFilhos = [3, 10, 1, 6, 14, 4, 7, 13]

for i in nosFilhos:
    raiz.insert(i)

raiz.visualizar_arvore()