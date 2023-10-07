from data_interaction import *
from menu import main_menu

Create()
with open('ascii-art.txt', 'r') as file:
    data = file.read()
print(data)
main_menu()

exit()

