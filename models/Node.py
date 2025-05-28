from graphviz import Digraph
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #Função de inserir na arvove os dados
    def insert(self, data):
        #Verifica se a Raiz tem alguma coisa
        if self.data is None:
            self.data = data
        
        else:
            #Varre a árvore para verificar se o nó está vazio e coloca no próx nó caso já esteja com algum dado
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
                            
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
    
    def inOrder(root):
        if root is None:
            return
        else:    
            inOrder(root.left)
            print(root.data)
            inOrder(root.right)
    
    
    # Funções para gerar imagem da árvore, utiliza a biblioteca graphviz para gerar a imagem
    def visualizar_arvore(self, filename="arvore_bst"):
        dot = Digraph()
        self._adicionar_nos(dot, self)
        dot.render(filename, format='png', cleanup=True)
        print(f"Árvore renderizada em: {filename}.png")
    
    def visualizar_inorder(self, filename="inorder_percorrido"):
        ordem = []

        def in_order(node):
            if node is None:
                return
            in_order(node.left)
            ordem.append(node.data)
            in_order(node.right)

        in_order(self)

        dot = Digraph(comment="Percurso InOrder")
        for i, val in enumerate(ordem):
            dot.node(str(i), str(val))
            if i > 0:
                dot.edge(str(i - 1), str(i))

        dot.render(filename, format='png', cleanup=True)
        print(f"Percurso inOrder renderizado em: {filename}.png")
    
    def _adicionar_nos(self, dot, node):
        if node is not None:
            dot.node(str(id(node)), str(node.data))
            if node.left:
                dot.node(str(id(node.left)), str(node.left.data))
                dot.edge(str(id(node)), str(id(node.left)))
                self._adicionar_nos(dot, node.left)
            if node.right:
                dot.node(str(id(node.right)), str(node.right.data))
                dot.edge(str(id(node)), str(id(node.right)))
                self._adicionar_nos(dot, node.right)
