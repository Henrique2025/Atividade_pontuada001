class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade
    #Lançar excecção.
    def _verificar_idade(self,idade):
        if idade <0:
            raise ValueError("Idade nao pode ser negativa.")
        if not isinstance(idade, int):
            raise TypeError("A idade deve contar apenas números.")
        return idade
    
    def __str__(self) -> str:
        return (f"\n Nome: {self.nome}"
                f"\n Idade: {self.idade}"
)
    