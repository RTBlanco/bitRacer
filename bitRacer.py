import time

car = """
    ______
 __/__|__\\___
|  _  _     _`-.
'-(_)------(_)--'
"""


def display():
  for i in range(20):
    print(f'{"." * i}{car}\r', end='')
    # print(f'{"." * i}\r', end='')

    time.sleep(0.1)
  print('\n')

display()