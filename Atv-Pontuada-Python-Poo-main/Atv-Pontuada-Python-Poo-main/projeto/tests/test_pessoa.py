import pytest

from projeto.models.pessoa import Pessoa


@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("Claudio", 22)

    return pessoa

def test_pessoa_alterar_nome_valido(pessoa_valida):
    
    pessoa_valida.nome = "Pedro"
    assert pessoa_valida.nome == "Pedro"

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Claudio"


def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida.idade == 22


def test_pessoa_idade_negativa_retorna_mensagem_excecao(pessoa_valida):
    #Mensagem de erro
    with pytest.raises(ValueError, match="Idade nao pode ser negativa."):
        Pessoa("Claudio",-1)
def test_pessoa_idade_tipo_invalido_retorna_mensagem_excecao(pessoa_valida):
    #Mensagem de erro
    with pytest.raises(TypeError, match="A idade deve contar apenas números."):
        Pessoa("Claudio","22")