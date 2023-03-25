class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
    def __str__(self):
        return f"Persona:\n Nome:{self.nome}\nCognome:{self.cognome}\nEtà:{self.eta}\n"

class Studente(Persona):
    def __init__(self, nome, cognome, eta, corso):
        Persona.__init__(nome,cognome,eta)
        self.corso = corso

    def __str__(self):
        return 'Studente:\n nome: %s\n cognome: %s\n eta: %s \n corso: %s\n' % (self.nome,self.cognome, str(self.eta),self.corso)

if __name__ == '__main__':
    x = Persona("federico", "calò", 25)
    print(x)

    y = Studente("federico", "calò", 25,"Informatica")
    print(y)
