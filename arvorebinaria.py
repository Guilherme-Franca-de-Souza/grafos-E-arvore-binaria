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
        self.totalnos = 0
    

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
                    arvore.totalnos += 1
            else:
                adress = adress*10
                if atual.esq != None:
                    self.inserir(atual.esq, novo, adress)
                else:
                    novo.adress = adress
                    atual.esq = novo
                    arvore.totalnos += 1
        else:
            arvore.raiz = novo
            arvore.raiz.adress = adress
            arvore.totalnos += 1
    
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

    def totalno(self, atual, parada):
        global cont
        print(f'cont: {cont}')
        if(atual != None):
            self.totalno(atual.esq, cont, parada)
            self.totalno(atual.dir, cont, parada)
            if atual.valor == parada:
                print(f'total de nós: {cont}')
                return cont 

    def remover(self, atual, pai, alvo):

        #função para repassar os valores de lugar
        def herda(alvo, pai, herdeiro):
            arvore.totalnos -=1
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
                    arvore.totalnos -= 1
                else:
                    pai.dir = None
                    arvore.totalnos -= 1


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
arvore.preorder(arvore.raiz)

#print("\n\nremove:")
#arvore.remover(arvore.raiz, None, 5)

#print("\n\nem ordem")
#arvore.inorder(arvore.raiz)

#arvore.buscar(arvore.raiz, 21)
#print(f'total de nos = {arvore.totalnos}')
#print(arvore.nomaximo(arvore.raiz))