class Laul:
    def __init__(self, esitaja, pealkiri, kuulamiste_arv):
        self.esitaja = esitaja
        self.pealkiri = pealkiri
        self.kuulamiste_arv = kuulamiste_arv

    def näita(self):
        print(f"Esitaja: {self.esitaja}, Pealkiri: {self.pealkiri}, Kuulamiste arv: {self.kuulamiste_arv}")
