# DESAFIO 26
# Faça um programa que leia uma frase pelo teclado e mostre:
#
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez

frase='Faça um programa que leia uma frase pelo teclado e mostre'
print(f'A letra "a" aparece:  {frase.count('a')} vezes')
print(f'A letra "a" aparece a primeira vez: {frase.find('a')+1}° posição')
print(f'A letra "a" aparece a ultima vez: {frase.rfind('a')+1}°posição')