import time, os, random

car = ["        ",
       "     ______       ",
       " __/__|__\\___    ",
       "|  _  _     _  `-.   ",
       " '-(_)------(_)--'"]


def drive(i, car):
  for line in car:
    print(f'{" " * i}{line}')


def display():
  increment = 1
  winner = random.randint(1, 3)
  print(winner)
  for i in range(120):
    if i >= 50:
      
      if winner == 1:
        drive((i + increment ), car)
        drive(i, car)  
      elif winner == 2:
        drive(i, car)
        drive((i + increment ), car)
      else:
        drive((i + increment ), car)
        drive((i + increment ), car)

      increment += 1
    else:
      drive(i, car)
      drive(i, car)
    
    time.sleep(0.001)
    os.system('cls||clear')

if __name__ == '__main__':
  display()
