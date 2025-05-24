#classe para criar o nó
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data;

#Função de inserir na arvove os dados
    def insert(self, data):
        #Verifica se a Raiz tem alguma coisa
        if self.data is None:
            self.data = data
        
        else:
            #Varre a árvore para verificar se o nó esta vazio e coloca no próx nó caso já esteje com algum dado
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