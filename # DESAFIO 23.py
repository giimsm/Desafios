# DESAFIO 23
# Faça um programa que leia um numero de 0 a 9999 e mostre
# na tela cada um dos dígitos separados.
#
# Ex: Digite um numero: 1834
#
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1
numero=input('Digite um numero entre 0 e 9999:\n')
if len(numero)==1:
    print(f'Unidade {numero[0]}')
elif len(numero)==2:
    print(f'Unidade: {numero[1:2]}')
    print(f'Dezena: {numero[0]}')
elif len(numero)==3:
    print(f'Unidade: {numero[2:3]}')
    print(f'Dezena: {numero[1:2]}')
    print(f'Centena {numero[0]}')
else:
    print(f'Unidade: {numero[3:4]}')
    print(f'Dezena: {numero[2:3]}')
    print(f'Centena: {numero[1:2]}')
    print(f'Milhar$ {numero[0]}')