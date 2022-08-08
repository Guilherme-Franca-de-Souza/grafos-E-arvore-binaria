'''

import random
import os

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
        return "\nno inserido com sucesso\n"
    
    def buscar(self, atual, valor):
        if(atual == None):
            return "arvore vazia"
        if(atual.valor != valor):
            if (valor > atual.valor):
                if(atual.dir != None):
                    return self.buscar(atual.dir, valor)
                else:
                    return "Esse valor nao existe"
            else:
                if(atual.esq != None):
                    return self.buscar(atual.esq, valor)
                else:
                    return "Esse valor nao existe"
        else:
            return atual.adress
    
    def nomaximo(self, atual):
        if(atual == None):
            return "arvore vazia"
        if(atual.dir != None):
            return self.nomaximo(atual.dir)
        else:
            return atual.valor

    def nominimo(self, atual):
        if(atual == None):
            return "arvore vazia"
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
            return "arvore vazia"
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

    def pre(self, atual, valor):
        if(atual == None):
            return "arvore vazia"
        if(atual.valor != valor):
            if (valor > atual.valor):
                if(atual.dir != None):
                   return self.pre(atual.dir, valor)
                else:
                    return ("Esse valor nao existe")
            else:
                if(atual.esq != None):
                   return self.pre(atual.esq, valor)
                else:
                    return ("Esse valor nao existe")
        else:
            return self.altura(atual) - 1

    def nivel(self, atual, valor):
        if(atual == None):
            return "arvore vazia"
        if(atual.valor != valor):
            if (valor > atual.valor):
                if(atual.dir != None):
                    return 1 + self.nivel(atual.dir, valor)
                else:
                    return "Esse valor nao existe"
            else:
                if(atual.esq != None):
                    return 1 + self.nivel(atual.esq, valor)
                else:
                    return "Esse valor nao existe"
        else:
            return 0

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
        if(atual == None):
            return "arvore vazia"
        #funções para repassar os valores de lugar
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
                if(alvo.dir != herdeiro):
                    herdeiro.dir = alvo.dir
                if(alvo.esq != herdeiro):
                    herdeiro.esq = alvo.esq
                arvore.raiz = herdeiro
        
        def reendereca(no):
            if(no.dir != None):
                no.dir.adress = no.adress * 10 + 1
                reendereca(no.dir)
            if(no.esq != None):
                no.esq.adress = no.adress * 10
                reendereca(no.esq)

        def repoe(herdeiro, herdeiropai, repositor):
            repositor.adress = herdeiro.adress
            reendereca(repositor)
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
                    return "Esse valor nao existe"
            else:
                if(atual.esq != None):
                    self.remover(atual.esq, atual, alvo)
                else:
                    return "Esse valor nao existe"
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
                    herdeiropai.esq = None
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
                    herdeiropai.dir = None
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


arvore = Arvore()



array = []
for i in range(0,15):
    array.append(i)

for i in range(0,15):
    valor = random.choice(array)
    array.remove(valor)
    no = No(valor)
    arvore.inserir(arvore.raiz, no, 1)


def digite():
    try:
        print("Digite o valor:")
        valor = input()
        valor = int(valor)
        return valor
    except:
        print("valor invalido")
        limpa()

def limpa():
    input("\n\n\ndigite enter para continuar...")
    os.system("cls")

while True:
    #os.system("cls")
    print("Digite uma opção:\n")
    print("(0) - Sair\n")
    print("(1) - Inserir no")
    print("(2) - Buscar posicao de um no")
    print("(3) - Percorrer arvore em ordem")
    print("(4) - Percorrer arvore pre ordem")
    print("(5) - Percorrer arvore pos ordem")
    print("(6) - Mostrar quantidade de nos")
    print("(7) - Mostrar quantidade de folhas")
    print("(8) - Mostrar quais nos sao folhas")
    print("(9) - Mostrar altura de um no")
    print("(10) - Mostrar nivel de um no")
    print("(11) - Remover no")
    
    folhas = []
    op = input()

    
    op = int(op)
    if(op < 0 or op > 11):
        print("opcao invalida")
    else:
        if op == 0:
            limpa()
            break
        elif op == 1:
            valor = digite()
            no = No(valor)
            print(arvore.inserir(arvore.raiz, no, 1))
            limpa()
        elif op == 2:
            valor = digite()
            print(f"Posicao de {valor}:")
            print(arvore.buscar(arvore.raiz, valor))
            limpa()
        elif op == 3:
            print("em ordem:\n")
            arvore.inorder(arvore.raiz)
            limpa()
        elif op == 4:
            print("pre ordem:\n")
            arvore.preorder(arvore.raiz)
            limpa()
        elif op == 5:
            print("pos ordem:\n")
            arvore.posorder(arvore.raiz)
            limpa()
        elif op == 6:
            print("Quantidade de nos:\n")
            print(arvore.totalno(arvore.raiz))
            limpa()
        elif op == 7:
            print("Quantidade de folhas:\n")
            print(arvore.totalfolhas(arvore.raiz))
            limpa()
        elif op == 8:
            print("Noses que sao folhas:\n")
            arvore.folhas(arvore.raiz)
            print(folhas)
            limpa()
        elif op == 9:
            valor = digite()
            print(f"Altura do no {valor}:")
            print(arvore.pre(arvore.raiz, valor))
            limpa()
        elif op == 10:
            valor = digite()
            print(f"Nivel do no {valor}:")
            print(arvore.nivel(arvore.raiz, valor))
            limpa()
        elif op == 11:
            valor = digite()
            arvore.remover(arvore.raiz, None, valor)
            limpa()
    
'''

import os

class Vertice():
    def __init__(self, nome):
        self.nome = nome
        

class Aresta():
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2


class Grafo():
    def __init__(self):
        self.vertices = []
        self.arestas = []


    def verificaaresta(self, v1, v2):
        for i in range(0, len(self.arestas)):
            if self.arestas[i].v1.nome == v1:
                if self.arestas[i].v2.nome == v2:
                    return ("existe uma aresta entre os vertices inforamdos") 
            if self.arestas[i].v2.nome == v1:
                if self.arestas[i].v1.nome == v2:
                    return ("existe uma aresta entre os vertices inforamdos") 
        return ('nao existe uam aresta entre os vertices informados')

    
    def inserirvertice(self, nome):
        for i in range(0, len(self.vertices)):
            if(self.vertices[i].nome == nome):
                return ("ja existe um vertice com esse nome")
        vertice = Vertice(nome)
        self.vertices.append(vertice)
        return ("vertice criado com sucesso")


    def inseriraresta(self, v1, v2):
        string = self.verificaaresta(v1,v2)
        if(string != 'existe uma aresta entre os vertices inforamdos'):            
            v1valido = False
            for i in range (0, len(self.vertices)):
                if self.vertices[i].nome == v1:
                    vertice1 = self.vertices[i]
                    v1valido = True
                    break
            if (v1valido):
                v2valido = False
                for i in range (0, len(self.vertices)):
                    if self.vertices[i].nome == v2:
                        vertice2 = self.vertices[i]
                        v2valido = True
                        break
                if (v2valido):
                    aresta = Aresta(vertice1, vertice2)
                    self.arestas.append(aresta)
                else:
                    print(f'O vertice " {v2} " nao existe')
            else:
                print(f'O vertice " {v1} " nao existe')
            return ("aresta incluida com sucesso")
        else:
            return ("Ja "+string)
    
    
    def removervertice(self, nome):
        for i in range(0, len(self.arestas)):
            if self.arestas[i].v1.nome == nome:
                self.arestas.pop(i)
            if self.arestas[i].v2.nome == nome:
                self.arestas.pop(i) 
        
        existe = False
        for i in rane(0, len(self.vertices)):
            if self.vertices[i].nome == nome:
                existe = True
                self.vertice.pop(i)
                break
        
        if existe == False:
            return "nao existe um vertice com esse nome"
        else:
            return "vertice removido com sucesso"
    
        
    
    def removearesta(self, v1, v2):
        for i in range(0, len(self.arestas)):
            if self.arestas[i].v1.nome == v1:
                if self.arestas[i].v2.nome == v2:
                    self.arestas.pop(i)
                    return("aresta removida com sucesso")
            if self.arestas[i].v2.nome == v1:
                if self.arestas[i].v1.nome == v2:
                    self.arestas.pop(i) 
                    return("aresta removida com sucesso")
        return ('nao existe uam aresta entre os vertices informados')
    
    def verticesadjacentes(self, nome):
        adjacentes = []
        for i in range(0, len(self.arestas)):
            if self.arestas[i].v1.nome == nome:
               adjacentes.append(self.arestas[i].v2.nome) 
            if self.arestas[i].v2.nome == nome:
               adjacentes.append(self.arestas[i].v1.nome)

        return adjacentes
    
    def grauvertice(self, nome):
        existe = False
        for i in range(0, len(self.vertices)):
            if(self.vertices[i].nome == nome):
                existe = True
                grau = 0
                for i in range(0, len(self.arestas)):
                    if self.arestas[i].v1.nome == nome:
                        grau += 1
                    if self.arestas[i].v2.nome == nome:
                        grau += 1
        if existe == False:
           return("nao existe um vertice com esse nome")
        else:
            return grau 
        
    
    def graumedio(self):
        qtd = len(self.vertices)
        if qtd > 0:
            grau = 0
            for i in range(0, len(self.vertices)):
                nome = self.vertices[i].nome
                for j in range(0, len(self.arestas)):
                    if self.arestas[j].v1.nome == nome:
                        grau += 1
                    if self.arestas[j].v2.nome == nome:
                        grau += 1
            return(grau/qtd)
        else:
            return 0

    def grauminimo(self):
        minimo = -1
        for i in range(0, len(self.vertices)):
            grau = 0
            nome = self.vertices[i].nome
            for j in range(0, len(self.arestas)):
                if self.arestas[j].v1.nome == nome:
                    grau += 1
                if self.arestas[j].v2.nome == nome:
                    grau += 1
            if minimo < 0:
                minimo = grau
            if grau < minimo:
                minimo = grau
        
        return minimo
    
    def graumaximo(self):
        maximo = -1
        for i in range(0, len(self.vertices)):
            grau = 0
            nome = self.vertices[i].nome
            for j in range(0, len(self.arestas)):
                if self.arestas[j].v1.nome == nome:
                    grau += 1
                if self.arestas[j].v2.nome == nome:
                    grau += 1
            if grau > maximo:
                maximo = grau
        return maximo



    def verificaconexo(self):
        qtd = len(self.vertices)
        if qtd > 0:
            lista = []
            conexos = self.conexo(self.vertices[0].nome, lista)
            if qtd > conexos:
                print("grafo nao conexo")
            else:
                print("grafo conexo")
        else:
            return("nao exsitem vertices no grafo")
    
    def conexo(self, nome, lista):
        verificado = False
        for i in range(0,len(lista)):
            if(nome == lista[i]):
                verificado = True
                break
        if verificado == False:
            
            lista.append(nome)
            adjacentes = []
            for j in range(0, len(self.arestas)):
                if self.arestas[j].v1.nome == nome:
                    verificado = False
                    for i in range(0,len(lista)):
                        if(self.arestas[j].v2.nome == lista[i]):
                            verificado = True
                            break
                    if verificado == False:
                        adjacentes.append(self.arestas[j].v2.nome)
    
                if self.arestas[j].v2.nome == nome:
                    verificado = False
                    for i in range(0,len(lista)):
                        if(self.arestas[j].v1.nome == lista[i]):
                            verificado = True
                            break
                    if verificado == False:
                        adjacentes.append(self.arestas[j].v1.nome)
                    
            for i in range(0,len(adjacentes)):
                self.conexo(adjacentes[i],lista)
                
            return len(lista)
                    
            
            
            
            
    def matriz(self):
        nomes = []
        for i in range(0, len(self.vertices)):
            nomes.append(self.vertices[i].nome)

        matriz = []
        linha = []
        for i in range(0, len(nomes)):
            for j in range(0, len(nomes)):
                resultado = self.verificaaresta(nomes[i],nomes[j])
                if resultado == "existe uma aresta entre os vertices inforamdos":
                    linha.append(1)
                else:
                    linha.append(0)
            matriz.append(linha)
            linha = []

        return matriz
    

    def verificaeuler(self):
        qtd = len(self.vertices)
        if qtd > 0:
            lista = []
            conexos = self.conexo(self.vertices[0].nome, lista)
            if qtd > conexos:
                print("Esse grafo nao eh conexo, portanto nao tem caminho de euler")
            else:
                print(self.euler())
                
        else:
            return("nao exsitem vertices no grafo")

    def euler(self):
        impares = 0
        for i in range(0,len(self.vertices)):
            resultado = self.grauvertice(self.vertices[i].nome)
            if(resultado%2 != 0):
                impares += 1
        
        if impares != 2 and impares != 0:
            return ("esse grafo nao tem caminho de euler")
        else:
            return ("Esse grafo tem caminho de euler") 
            
                
                
                



    
                
        
                    


grafo = Grafo()
    
def digite(qtd):
    if qtd == 0:
        print("Digite o nome:")
        valor = input()
        return valor
        limpa()
    if qtd == 1:
        print("Digite o nome do primeiro vertice:")
        valor = input()
        return valor
        limpa()
    if qtd == 2:
        print("Digite o nome do segundo vertice:")
        valor = input()
        return valor
        
    
        
        
def limpa():
    input("\n\n\ndigite enter para continuar...")
    os.system("clear")
               


while True:
    #os.system("cls")
    print("Digite uma opção:\n")
    print("(0) - Sair\n")
    print("(1) - Inserir verice")
    print("(2) - Inserir aresta")
    print("(3) - Verificar existencia de aresta")
    print("(4) - Remover vertice")
    print("(5) - Remover aresta")
    print("(6) - Verificar grau de vertice")
    print("(7) - Verificar vertices adjacentes")
    print("(8) - Mostrar grau medio")
    print("(9) - Mostrar grau maximo")
    print("(10) - Mostrar grau minimo")
    print("(11) - Verificar se o grafo eh conexo")
    print("(12) - Verificar se existe caminho de euler no grafo")
    print("(13) - Matriz de adjacencias")
    
    
    
    
    

    op = input()
    
    op = int(op)
    if(op < 0 or op > 11):
        print("opcao invalida")
    else:
        if op == 0:
            limpa()
            break
        elif op == 1:
            valor = digite(0)
            vertice = Vertice(valor)
            print(grafo.inserirvertice(valor))
            limpa()
        elif op == 2:
            valor1 = digite(1)
            valor2 = digite(2)
            print(grafo.inseriraresta(valor1,valor2))
            limpa()
        elif op == 3:
            valor1 = digite(1)
            valor2 = digite(2)
            print(grafo.verificaaresta(valor1,valor2))
            limpa()
        elif op == 4:
            valor = digite(0)
            print(grafo.removervertice(valor))
            limpa()
        elif op == 5:
            valor1 = digite(1)
            valor2 = digite(2)
            print(grafo.removearesta(valor1,valor2))
            limpa()
        elif op == 6:
            valor = digite(0)
            print(grafo.grauvertice(valor))
            limpa()
        elif op == 7:
            valor = digite(0)
            print(grafo.verticesadjacentes(valor))
            limpa()
        elif op == 8:
            print(grafo.graumedio())
            limpa()
        elif op == 9:
            print(grafo.graumaximo())
            limpa()
        elif op == 10:
            print(grafo.grauminimo())
            limpa()
        elif op == 11:
            grafo.verificaconexo()
            limpa()
        elif op == 12:
            print(grafo.verificaeuler())
            limpa()
        elif op == 13:
            print(grafo.matriz())
            limpa()
