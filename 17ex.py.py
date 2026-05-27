# ======================================================
# MÓDULO 1 — CRIAÇÃO DE STRINGS
# ======================================================

# EX1
# Crie uma variável chamada texto1 com o valor "Logica"
# usando aspas duplas e exiba o conteúdo.
texto1 = "Logica"
print("EX1:", texto1)

# EX2
# Crie uma variável chamada texto2 com o valor
# 'Eu sou top em python' usando aspas simples e exiba.
texto2 = 'Eu sou top em python'
print("EX2:", texto2) 

# EX3
# Crie uma string usando aspas simples que contenha
# aspas duplas dentro do texto: copa "padrão fifa".
texto3 = 'copa "padrão fifa"'
print("EX3:", texto3)

# EX4
# Crie uma string usando aspas duplas que contenha
# aspas simples dentro do texto: copa 'padrão fifa'.
texto4 = "copa 'padrão fifa'"
print("EX4:", texto4)


# ======================================================
# MÓDULO 2 — STRINGS MULTILINHA
# ======================================================

# EX5
# Crie uma string multilinha representando um menu
# com as opções:
# -A  Exibe ajuda
# -E  Execute agora, quero jogar!
menu = """-A  Exibe ajuda
-E  Execute agora, quero jogar!"""
print("\nEX5:\n" + menu)

# EX6
# Crie uma string multilinha contendo um poema
# com três versos.
poema = '''Batatinha quando nasce
Esparrama pelo chão
Menininha quando dorme
Põe a mão no coração'''
# Nota: Adicionei um quarto verso clássico pelo ritmo, mas os 3 versos principais estão aí!
print("\nEX6:\n" + poema)


# ======================================================
# MÓDULO 3 — CONCATENAÇÃO AUTOMÁTICA
# ======================================================

# EX7
# Use concatenação automática de literais para unir
# as palavras "Volei" e "top!".
# No Python, literais de string lado a lado são concatenados automaticamente.
concat1 = "Volei " "top!"
print("\nEX7:", concat1)

# EX8
# Concatene automaticamente as strings
# "Python", " é ", "demais" em uma única string.
concat2 = "Python" " é " "demais"
print("EX8:", concat2)


# ======================================================
# MÓDULO 4 — STRINGS COMO SEQUÊNCIAS
# ======================================================

# EX9
# Atribua "software" a uma variável chamada st
# e mostre a primeira letra da string.
st = "software"
print("\nEX9:", st[0])

# EX10
# Usando a mesma string "software",
# mostre a última letra.
print("EX10:", st[-1])

# EX11
# Mostre os caracteres do índice 1 até o índice 4
# (sem incluir o 4) da string "software".
print("EX11:", st[1:4])

# EX12
# Mostre os caracteres do início até o índice 3
# da string "software".
print("EX12:", st[:3])

# EX13
# Mostre os caracteres do índice 2 até o final
# da string "software".
print("EX13:", st[2:])

# EX14
# Mostre o tamanho da string "software"
# usando a função len().
print("EX14:", len(st))

# EX15
# Acesse o último caractere de "software"
# usando índice positivo (sem usar -1).
# O último índice é sempre (tamanho da string - 1)
ultimo_indice = len(st) - 1
print("EX15:", st[ultimo_indice])

# EX16
# Mostre os caracteres que estão nos índices pares
# da string "software".
# Sintaxe: [início:fim:passo] -> passo 2 pega os pares
print("EX16:", st[::2])

# EX17
# Inverta a string "software".
# Passo negativo inverte a sequência
print("EX17:", st[::-1])
