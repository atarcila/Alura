import random

# Definindo o número secreto
numero_secreto = random.randint(1, 100)

# Iniciando o loop do jogo
palpite = None
while palpite != numero_secreto:
  # Obtendo o palpite do usuário
  palpite = int(input("Digite seu palpite (entre 1 e 100): "))

  # Fornecendo pistas
  if palpite < numero_secreto:
    print("Seu palpite está muito baixo!")
  elif palpite > numero_secreto:
    print("Seu palpite está muito alto!")
  else:
    print("Parabéns! Você adivinhou o número secreto!")

# Mostrando o número secreto após o sucesso
print(f"O número secreto era: {numero_secreto}")