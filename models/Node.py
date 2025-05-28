from graphviz import Digraph
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
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

    # Em ordem
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.data)
        if self.right:
            self.right.in_order()

    def visualizar_arvore(self, filename="arvore_bst"):
        dot = Digraph()
        self._adicionar_nos(dot, self)
        dot.render(filename, format='png', cleanup=True)
        print(f"Árvore renderizada em: {filename}.png")

    def visualizar_inorder(self, filename="inorder_percorrido"):
        self._visualizar_percurso(self._coletar_inorder(), filename, "Percurso InOrder")

    def visualizar_preorder(self, filename="preorder_percorrido"):
        self._visualizar_percurso(self._coletar_preorder(), filename, "Percurso PreOrder")

    def visualizar_postorder(self, filename="postorder_percorrido"):
        self._visualizar_percurso(self._coletar_postorder(), filename, "Percurso PostOrder")

    # Funções para percorrer a arvore:
    def _coletar_inorder(self):
        ordem = []
        def in_order(node):
            if node:
                in_order(node.left)
                ordem.append(node.data)
                in_order(node.right)
        in_order(self)
        return ordem

    def _coletar_preorder(self):
        ordem = []
        def pre_order(node):
            if node:
                ordem.append(node.data)
                pre_order(node.left)
                pre_order(node.right)
        pre_order(self)
        return ordem

    def _coletar_postorder(self):
        ordem = []
        def post_order(node):
            if node:
                post_order(node.left)
                post_order(node.right)
                ordem.append(node.data)
        post_order(self)
        return ordem

    def _visualizar_percurso(self, ordem, filename, comment):
        dot = Digraph(comment=comment)
        for i, val in enumerate(ordem):
            dot.node(str(i), str(val))
            if i > 0:
                dot.edge(str(i - 1), str(i))
        dot.render(filename, format='png', cleanup=True)
        print(f"{comment} renderizado em: {filename}.png")

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
