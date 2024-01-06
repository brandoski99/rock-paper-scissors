import random
puntaje_c = 0
puntaje_p = 0
player = ''
while player != 'e':
   player = input("inserte el valor 'p' para papel 'r' para piedra y 't' para tijeras o 'e' para salir: ")
   computer = random.choice(['p', 'r', 't'])
   if computer == 'p' and player == 'r': 
      print("La computadora saco papel y tu piedra, la computadora gana")
      puntaje_c += 1
   elif computer == 'r' and player == 't':
      print("La computadora saco piedra y tu tijeras, la computadora gana")
      puntaje_c += 1
   elif computer == 't' and player == 'p':
      print("La computadora saco tijeras y tu papel, la computadora gana")
      puntaje_c += 1
   elif computer == 'p' and player == 't':
      print("La computadora saco papel y tu tijeras, Ganaste!")
      puntaje_p += 1
   elif computer == 'r' and player == 'p':
      print("La computadora saco piedra y tu papel, Ganaste!")
      puntaje_p += 1
   elif computer == 't' and player == 'r':
      print("La computadora saco tijeras y tu piedra, Ganaste!")
      puntaje_p += 1
   elif computer == player:
      print("Sacaron lo mismo, Empate!")

       	 
print(f"Ganaste: {puntaje_p} y Perdiste: {puntaje_c}")
