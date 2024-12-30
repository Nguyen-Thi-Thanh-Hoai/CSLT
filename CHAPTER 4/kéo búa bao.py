import random

def main():
  
  choices = ["kéo", "búa", "bao"]

 
  while True:
    
    player = int(input("Human: "))
    if 0<=player<4:
         player = int(input("Human: "))
   
    computer = random.randint(1, 3)
    print("Computer:",computer)

    
    if player == 0:
      break
    if player == computer:
      print("Draw!")
    elif (player == 1 and computer == 3) or (player == 2 and computer== 1) or (player== 3 and computer == 2):
      print("Human Win!")
    else:
      print("Computer Win!")

if __name__ == "__main__":
  main()