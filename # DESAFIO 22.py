# DESAFIO 22
# Crie um programa que leia o nome completo de uma pessoas
# e mostre
#
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome
nome=input('Digite o seu nome')
print('O nome em maiusculo: ',nome.upper())
print('O nome em minusculo',nome.lower())
print(f'O nome sem os espaços tem {len(nome.replace(" ", ""))}')
nomedividido=nome.split()
print(nomedividido)
print('O tamanho do primeiro nome',len(nomedividido[0]))



