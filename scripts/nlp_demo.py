import re

texto = input("Ingresá un texto: ")

texto = texto.lower()
texto = re.sub(r'[^a-záéíóúñü\s]', '', texto)

tokens = texto.split()

print("Tokens limpios:")
print(tokens)