class Cena:
    def __init__(self, id, descri):
        self.id = id
        self.descri = descri
        self.proximo = None

class Escolha:
    def __init__(self, escolha):
        self.escolha = escolha
        self.proximo = None

class No:
    def __init__(self,id, data):
        self.id = id
        self.data = data
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def inserir(self, no, id, data):
        if not no:
            return No(id, data)


        if id < no.id:
            no.esquerda = self.inserir(no.esquerda, id, data)
        else:
            no.direita = self.inserir(no.direita, id, data)


        no.altura = 1 + max(self.obter_altura(no.esquerda), self.obter_altura(no.direita))


        fator_balanceamento = self.obter_balanceamento(no)


        if fator_balanceamento > 1 and id < no.esquerda.id:
            return self.rotacionar_direita(no)
        if fator_balanceamento < -1 and id > no.direita.id:
            return self.rotacionar_esquerda(no)
        if fator_balanceamento > 1 and id > no.esquerda.id:
            no.esquerda = self.rotacionar_esquerda(no.esquerda)
            return self.rotacionar_direita(no)
        if fator_balanceamento < -1 and id < no.direita.id:
            no.direita = self.rotacionar_direita(no.direita)
            return self.rotacionar_esquerda(no)


        return no


    def remover(self, no, id):
        if not no:
            return no


        if id < no.id:
            no.esquerda = self.remover(no.esquerda, id)
        elif id > no.id:
            no.direita = self.remover(no.direita, id)
        else:
            if not no.esquerda:
                return no.direita
            elif not no.direita:
                return no.esquerda


            temp = self.obter_no_minimo(no.direita)
            no.id = temp.id
            no.data = temp.data
            no.direita = self.remover(no.direita, temp.id)


        no.altura = 1 + max(self.obter_altura(no.esquerda), self.obter_altura(no.direita))


        fator_balanceamento = self.obter_balanceamento(no)


        if fator_balanceamento > 1 and self.obter_balanceamento(no.esquerda) >= 0:
            return self.rotacionar_direita(no)
        if fator_balanceamento < -1 and self.obter_balanceamento(no.direita) <= 0:
            return self.rotacionar_esquerda(no)
        if fator_balanceamento > 1 and self.obter_balanceamento(no.esquerda) < 0:
            no.esquerda = self.rotacionar_esquerda(no.esquerda)
            return self.rotacionar_direita(no)
        if fator_balanceamento < -1 and self.obter_balanceamento(no.direita) > 0:
            no.direita = self.rotacionar_direita(no.direita)
            return self.rotacionar_esquerda(no)


        return no

    def mostrar_resultado(self, no, fila):
        if fila.head is not None and no is not None:
            if fila.head.escolha == 0:
                fila.remover_escolha()
                return self.mostrar_resultado(no.esquerda,fila)
            else:
                fila.remover_escolha()
                return self.mostrar_resultado(no.direita,fila)

        return no

    def buscar(self, no, id):
        if not no or no.i == id:
            return no
        if id < no.id:
            return self.buscar(no.esquerda, id)
        return self.buscar(no.direita, id)


    def rotacionar_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self.obter_altura(z.esquerda), self.obter_altura(z.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        return y


    def rotacionar_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self.obter_altura(z.esquerda), self.obter_altura(z.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        return y


    def obter_altura(self, no):
        if not no:
            return 0
        return no.altura


    def obter_balanceamento(self, no):
        if not no:
            return 0
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)


    def obter_no_minimo(self, no):
        if no is None or no.esquerda is None:
            return no
        return self.obter_no_minimo(no.esquerda)

    def pre_order(self, raiz, nivel = 0, lado = "Raiz"):
        if raiz is not None:
            print("-" * (nivel * 4) + f"[{lado}] -> {raiz.id} (Dado: {raiz.data}) {raiz.altura}")
            self.pre_order(raiz.esquerda, nivel + 1, "Esquerda")
            self.pre_order(raiz.direita, nivel + 1, "Direita")

class ListaDeCenas:
    def __init__(self):
        self.head = None
        self.iniciar_lista()

    def iniciar_lista(self):
        cenarios = [
            "Cena1",
            "Cena2",
            "Cena3",
            "Cena4",
            "Cena5"
        ]

        for id, desc in enumerate(cenarios, 1):
            self.adicionar_cena(id, desc)

    def adicionar_cena(self, id, desc):
        nova_cena = Cena(id, desc)
        if not self.head:
            self.head = nova_cena
            return
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = nova_cena

    def remover_cena(self, id):
        atual = self.head
        anterior = None
        while atual and atual.id != id:
            anterior = atual
            atual = atual.proximo
        if atual is None:
            print("Cena não encontrada.")
            return
        if anterior is None:
            self.head = atual.proximo
        else:
            anterior.proximo = atual.proximo
        print(f"Cena com ID {id} removida.")

    def buscar(self, id):
        atual = self.head
        while atual:
            if atual.id == id:
                return atual
            atual = atual.proximo
        
        print("Cena não encontrada")
        return None

    def mostrar_cenas(self):
        cena = self.head
        while cena:
            print(f"{cena.descri} || {cena.id}")
            cena = cena.proximo

class FilaDeEscolhas:
    def __init__(self):
        self.head = None

    def adicionar_escolha(self, escolha):
        nova_escolha = Escolha(escolha)
        if not self.head:
            self.head = nova_escolha
            return
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = nova_escolha

    def remover_escolha(self):
        if self.head is not None:
            self.head = self.head.proximo
            print("Escolha removida da fila!\n")
            return
        
        print("A fila não existe")

    def mostrar_escolhas(self):
        escolha = self.head
        while escolha:
            print(escolha.escolha)
            escolha = escolha.proximo

    def limpar(self):
        self.head = None

    def copiar(self):
        return self.head

    def colar(self, no):
        self.head = no

class PilhaDeEscolhas:
    def __init__(self):
        self.head = None

    def adicionar_escolha(self, escolha):
        nova_escolha = Escolha(escolha)
        if not self.head:
            self.head = nova_escolha
            return
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = nova_escolha

    def remover_da_pilha(self):
        self.head = self._remover(self.head)
        
    def _remover(self, item):
        if item.proximo:
            item.proximo = self._remover(item.proximo)
            return item
        
        return None

    def mostrar_escolhas(self):
        escolha = self.head
        while escolha:
            print(escolha.escolha)
            escolha = escolha.proximo

        

    def limpar(self):
        print("limpo")
        self.head = None

    def copiar(self):
        return self.head

    def colar(self, no):
        self.head = no

def jogo(lista, pilha, fila, tree, root):
    nivel = 1
    while True:
        cena_atual = lista.buscar(nivel)
        if cena_atual is not None:
            print(f"\n{cena_atual.descri}")
                    
            escolha = int(input("Qual a sua escolha:"))
            if escolha == 0 or escolha == 1:
                pilha.adicionar_escolha(escolha)
                nivel = nivel + 1
            else:
                print("Número invalido")
        else:
            fila.colar(pilha.copiar())
            fila.mostrar_escolhas()
            resultado = tree.mostrar_resultado(root, fila)
            print(resultado.data)
            print("Fim do Jogo")
            break

def main():
    tree = ArvoreAVL()
    root = None
    for id in range(1,64):
        # para adicionar os finais, você precisa ver qual a raiz que vc pode colacar o final (elas tem altura 1 que é informada no console depois do dado) 
        # e colocar o id nesse "switch".
        if id == 1:
            data = "Todo mundo morreu!"
            root = tree.inserir(root, id, data)
        elif id == 63:
            data = "Todo mundo viveu!"
            root = tree.inserir(root, id, data)
        else:
            data = f"Info {id}"
            root = tree.inserir(root, id, data)
    
    tree.pre_order(root)
    lista = ListaDeCenas()
    fila = FilaDeEscolhas()
    pilha = PilhaDeEscolhas()

    while True:
        fila.limpar()
        pilha.limpar()

        print("Escolha uma opção abaixo\n")
        print("1.Jogar")
        print("2.mostrar cenas")
        print("3.Sair\n")
        try:
            escolha =  int(input("faça sua escolha:"))
            if escolha == 1:
                jogo(lista, pilha, fila, tree, root)
                    
            elif escolha == 2:
                lista.mostrar_cenas()
            elif escolha == 3:
                print("\nSaindo do jogo!\n")
                break

        except ValueError:
            print("\nEntrada invalida\n")

if __name__ == '__main__':
    main()