import random


class No():
    def __init__(self, valor):
        self.valor = valor
        self.adress = None
        self.dir = None
        self.esq = None
        

class Arvore():
    def __init__(self):
        self.raiz = None
    

    def inorder(self, atual):
        if(atual != None):
            self.inorder(atual.esq)
            print("valor: ",atual.valor)
            print("endereco: ",atual.adress,"\n")
            self.inorder(atual.dir)

    def preorder(self, atual):
        if(atual != None):
            print("valor: ",atual.valor)
            print("endereco: ",atual.adress,"\n")
            self.preorder(atual.esq)
            self.preorder(atual.dir)

    def posorder(self, atual):
        if(atual != None):
            self.posorder(atual.esq)
            self.posorder(atual.dir)
            print("valor: ",atual.valor)
            print("endereco: ",atual.adress,"\n")
    
    def inserir(self, atual, novo, adress):
        if atual != None:
            if novo.valor > atual.valor:
                adress = (adress*10)+1
                if atual.dir != None:
                    self.inserir(atual.dir, novo, adress)
                else:
                    novo.adress = adress
                    atual.dir = novo
            else:
                adress = adress*10
                if atual.esq != None:
                    self.inserir(atual.esq, novo, adress)
                else:
                    novo.adress = adress
                    atual.esq = novo
        else:
            arvore.raiz = novo
            arvore.raiz.adress = adress
    
    def buscar(self, atual, valor):
        if(atual.valor != valor):
            if (valor > atual.valor):
                if(atual.dir != None):
                    self.buscar(atual.dir, valor)
                else:
                    print("Esse valor nao existe")
            else:
                if(atual.esq != None):
                    self.buscar(atual.esq, valor)
                else:
                    print("Esse valor nao existe")
        else:
            return atual.adress
    
    def nomaximo(self, atual):
        if(atual.dir != None):
            return self.nomaximo(atual.dir)
        else:
            return atual.valor


    def nominimo(self, atual):
        if(atual.esq != None):
            return self.nominimo(atual.esq)
        else:
            return atual.valor

    def totalno(self, atual):
        if(atual == None):
            return 0
        else:
            if(atual.esq != None and atual.dir != None):
                return 1 + self.totalno(atual.esq) + self.totalno(atual.dir)
            elif(atual.esq != None and atual.dir == None):
                return 1 + self.totalno(atual.esq) 
            elif(atual.esq == None and atual.dir != None):
                return 1 + self.totalno(atual.dir)
            else:
                return 1

    def totalfolhas(self, atual):
        if(atual == None):
            return 0
        else:
            if(atual.esq != None and atual.dir != None):
                return 0 + self.totalfolhas(atual.esq) + self.totalfolhas(atual.dir)
            elif(atual.esq != None and atual.dir == None):
                return 0 + self.totalfolhas(atual.esq) 
            elif(atual.esq == None and atual.dir != None):
                return 0 + self.totalfolhas(atual.dir)
            else:
                return 1        

    def folhas(self, atual):
        def lista(valor):
            folhas.append(valor)

        if(atual == None):
            return 0
        else:
            if(atual.esq != None and atual.dir != None):
                return self.folhas(atual.esq) + self.folhas(atual.dir)
            elif(atual.esq != None and atual.dir == None):
                return self.folhas(atual.esq) 
            elif(atual.esq == None and atual.dir != None):
                return self.folhas(atual.dir)
            else:
                lista(atual.valor)
                return 1

    def prealtura(self, atual, valor):
        if(atual.valor != valor):
            if (valor > atual.valor):
                if(atual.dir != None):
                   return self.prealtura(atual.dir, valor)
                else:
                    print("Esse valor nao existe")
            else:
                if(atual.esq != None):
                   return self.prealtura(atual.esq, valor)
                else:
                    print("Esse valor nao existe")
        else:
            return self.altura(atual) - 1


    def altura(self, atual):
        if(atual.esq != None and atual.dir != None):
            direita = self.altura(atual.dir)
            esquerda = self.altura(atual.esq)
            if(direita > esquerda):
                return 1 + self.altura(atual.dir)
            else:
                return 1 + self.altura(atual.esq)
        elif(atual.esq != None and atual.dir == None):
            return 1 + self.altura(atual.esq) 
        elif(atual.esq == None and atual.dir != None):
            return 1 + self.altura(atual.dir)
        else:
            return 1



    def remover(self, atual, pai, alvo):

        #função para repassar os valores de lugar
        def herda(alvo, pai, herdeiro):
            herdeiro.adress = alvo.adress
            if(pai != None):
                if(alvo.dir != herdeiro):
                    herdeiro.dir = alvo.dir
                if(alvo.esq != herdeiro):
                    herdeiro.esq = alvo.esq
                if(alvo.valor > pai.valor):
                    pai.dir = herdeiro 
                else:
                    pai.esq = herdeiro
            else:
                arvore.raiz = None

        def repoe(herdeiro, herdeiropai, repositor):
            repositor.adress = herdeiro.adress
            if(herdeiro.valor > herdeiropai.valor):
                herdeiropai.dir = repositor 
            else:
                herdeiropai.esq = repositor
 
        # PROCURA O VALOR
        if(atual.valor != alvo):
            if (alvo > atual.valor):
                if(atual.dir != None):
                    self.remover(atual.dir, atual, alvo)
                else:
                    print("Esse valor nao existe")
            else:
                if(atual.esq != None):
                    self.remover(atual.esq, atual, alvo)
                else:
                    print("Esse valor nao existe")
        else:
            alvo = atual
        # DELETA
            if(alvo.dir != None):
                if(alvo.dir.esq != None):
                    herdeiro = alvo.dir.esq
                    herdeiropai = alvo.dir
                    digno = False
                    while (digno != True):
                        if(herdeiro.esq != None):
                            herdeiropai = herdeiro
                            herdeiro = herdeiro.esq
                        else:
                            digno = True
                    if(herdeiro.dir != None):
                        repoe(herdeiro, herdeiropai, herdeiro.dir)
                    herda(alvo, pai, herdeiro)
                else:
                    herdeiro = alvo.dir
                    herda(alvo, pai, herdeiro)
            elif(alvo.esq != None):
                if(alvo.esq.dir != None):
                    herdeiro = alvo.esq.dir
                    herdeiropai = alvo.esq
                    digno = False
                    while (digno != True):
                        if(herdeiro.dir != None):
                            herdeiropai = herdeiro
                            herdeiro = herdeiro.dir
                        else:
                            digno = True
                    if(herdeiro.esq != None):
                        repoe(herdeiro, herdeiropai, herdeiro.esq)
                    herda(alvo, pai, herdeiro)
                else:
                    herdeiro = alvo.esq
                    herda(alvo, pai, herdeiro)

            else:
                if(pai.valor > alvo.valor):
                    pai.esq = None
                else:
                    pai.dir = None



array = []

for i in range(0,15):
    array.append(i)

arvore = Arvore()


for i in range(0,15):
    valor = random.choice(array)
    array.remove(valor)
    no = No(valor)
    arvore.inserir(arvore.raiz, no, 1)





#print("\n\nem ordem")
#print(arvore.totalno(arvore.raiz))
#arvore.remover(arvore.raiz, None, 5)
arvore.inorder(arvore.raiz)
folhas = []
#arvore.folhas(arvore.raiz)
#print(f"as folhas sao: {folhas}")
print(arvore.prealtura(arvore.raiz, 4))


#print("\n\nremove:")
#arvore.remover(arvore.raiz, None, 5)

#print("\n\nem ordem")
#arvore.inorder(arvore.raiz)

#arvore.buscar(arvore.raiz, 21)
#print(f'total de nos = {arvore.totalnos}')
#print(arvore.nomaximo(arvore.raiz))