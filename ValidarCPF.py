# Lê o cpf que o usuario inserir e já formando uma lista.
cpf = input('Digite um cpf (Sómente números): ')
cpfInserido = cpf


# Cria a função
def calcular(cpf_list):
    n = 10
    cod = 0

    # Utiliza uma estrutura de repetição para percorrer cada item da lista executando um código determinado
    # em cada item.
    # O código inserido nesta estrutura é o calculo para validar o cpf
    for x in cpf_list[0:9]:
        cod += int(x) * n
        n -= 1

    # Calcula o penultimo numero e já o insere em sua posição do cpf dentro da lista.
    if (11 - cod % 11) >= 10:
        cpf_list[9] = str(0)
    else:
        cpf_list[9] = str(11 - cod % 11)

    n = 11
    cod = 0

    # Calcula o ultimo numero
    for x in cpf_list[0:10]:
        cod += int(x) * n
        n -= 1

    # Fal o calulo para descobrir qual é o ultimo numero e o inserir em sua posição dentro da lista.
    if (11 - cod % 11) >= 10:
        cpf_list[10] = str(0)
    else:
        cpf_list[10] = str(11 - cod % 11)

    # Retorna a lista valida
    return cpf_list


if list(cpfInserido) == calcular(list(cpf)):
    print('O cpf inserido é válido!')
else:
    print('O cpf inserido não é válido!')
