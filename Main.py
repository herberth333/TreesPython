from models.Node import Node
                    
# Exemplo de uso:
raiz = Node(8)
nosFilhos = [8, 9, 24, 55, 12, 3, 4, 13]

for i in nosFilhos:
    raiz.insert(i)

# raiz.visualizar_arvore()
raiz.visualizar_inorder()