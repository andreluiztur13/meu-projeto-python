
class Celular():
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor 
        self.ano = ano
    
    def __str__(self):
        return f"Este celular tem a marcar {self.marca}, modelo {self.modelo}, cor {self.cor} e ano {self.ano}."
    
    def telefonar_contato(self, contato):
        print(f"Você está ligando para {contato}.")

    def telefonar_numero(self, numero):
        print(f"Você está ligando para o número {numero}.")



cel_andre = Celular('Motorola', 'MotoG', 'azul', 2023)

print(cel_andre.ano)

print(cel_andre)

cel_andre.telefonar_contato('mãe')
cel_andre.telefonar_numero(993859841)







