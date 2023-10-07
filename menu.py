from data_interaction import *

c1 = 'Add animal'
c2 = 'Add command(s) to animal'
c3 = 'Show trained commands of animal'
c4 = 'Remove animal'
c5 = 'List of animals'
c6 = 'Exit'

menu_options = {
    1: c1,
    2: c2,
    3: c3,
    4: c4,
    5: c5,
    6: c6
}


# view_options = {
#     1: cv1,
#     2: cv2,
#     3: cv3,
#     4: cv4,
# }


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    print(c1, '\n')
    AddAnimal(c)
    main_menu()


def option2():
    print(c2, '\n')
    AddCommand()
    main_menu()


def option3():
    print(c3, '\n')
    ViewCommand()
    main_menu()


def option4():
    print(c4, '\n')
    RemoveAnimalByName()
    main_menu()


def option5():
    print(c5, '\n')
    ViewAnimals()
    main_menu()


def option6():
    print(c6, '\n')


def main_menu():
    print_menu()
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')
    # Check what choice was entered and act accordingly
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5:
        option5()
    elif option == 6:
        print('\nHave a good day!')
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 6.')
