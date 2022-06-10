cpf = input('Digite um cpf (Sómente números): ')
cpfInserido = cpf


def calcular(cpf_list):
    n = 10
    cod = 0

    for x in cpf_list[0:9]:
        cod += int(x) * n
        n -= 1

    if (11 - cod % 11) >= 10:
        cpf_list[9] = str(0)
    else:
        cpf_list[9] = str(11 - cod % 11)

    n = 11
    cod = 0

    for x in cpf_list[0:10]:
        cod += int(x) * n
        n -= 1

    if (11 - cod % 11) >= 10:
        cpf_list[10] = str(0)
    else:
        cpf_list[10] = str(11 - cod % 11)

    return cpf_list


if list(cpfInserido) == calcular(list(cpf)):
    print('O cpf inserido é válido!')
else:
    print('O cpf inserido não é válido!')
