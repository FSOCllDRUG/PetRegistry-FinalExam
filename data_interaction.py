import csv
import os
import os.path
from prettytable import PrettyTable

header = ['Type of animal', 'Animal', 'Name', 'Age', 'Commands']
table = PrettyTable()


class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1


c = Counter()


# Creating data.csv if it doesn't exist
def Create():
    if os.path.isfile('data.csv') == False:
        with open('data.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(header)


# Append data.csv by adding new note(row)
def AddAnimal(c):
    animal = input('What animal is this? ')
    typeof = ClassifyAnimal(animal)
    name = input('What is the name of this animal? ')
    age = input('How old is this animal? ')
    commands = input('What commands does this animal know? ')
    row = {'Type of animal': typeof, 'Animal': animal, 'Name': name, 'Age': age, 'Commands': commands}

    # Open the CSV file in "append" mode
    with open('data.csv', 'a', newline='') as f:
        # Create a dictionary writer with the dict keys as column fieldnames
        writer = csv.DictWriter(f, fieldnames=row.keys())

        # Append single row to CSV
        writer.writerow(row)
    # Increment counter
    c.add()


# Function for classification type of animal by 'animal'
def ClassifyAnimal(animal):
    animal_dict = {
        'horse': 'Pack',
        'camel': 'Pack',
        'donkey': 'Pack',
        'cat': 'Domestic',
        'dog': 'Domestic',
        'hamster': 'Domestic'
    }
    animal_type = animal_dict.get(animal.lower(), None)
    if animal_type is None:
        print(f'{animal} cannot be classified.')
    else:
        return animal_type


# Function for printing out all listed animals
def ViewAnimals():
    r = csv.reader(open('data.csv'))
    lines = list(r)
    table = PrettyTable()
    table.field_names = lines[0]
    table.add_rows(lines[1:])
    print(table)


# Function for adding command(s) by animal name
def AddCommand():
    r = csv.reader(open('data.csv'))
    lines = list(r)
    sname = str(input('Enter name of animal: '))
    sline = SearchRowByName(sname)
    if sline is None:
        print('Name not found. Returning to menu.')
        return
    edited_note = str(input('Enter edited note: '))
    if lines[sline][4]:
        lines[sline][4] += ", " + edited_note
    else:
        lines[sline][4] += edited_note
    writer = csv.writer(open('data.csv', 'w', encoding='UTF8', newline=''))
    writer.writerows(lines)


# Function for searching row id in column 'Name' by entered animal name
def SearchRowByName(sname):
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if sname == row[2]:
                return i


# Function for deleting selected by id note
def RemoveAnimalByName():
    r = csv.reader(open('data.csv'))
    lines = list(r)
    # print(lines)
    sname = str(input('Enter name of animal to delete: '))
    lines.pop(SearchRowByName(sname))
    writer = csv.writer(open('data.csv', 'w', encoding='UTF8', newline=''))
    writer.writerows(lines)


def ViewCommand():
    r = csv.reader(open('data.csv'))
    lines = list(r)
    sname = str(input('Enter name of animal to check commands: '))
    sline = SearchRowByName(sname)
    if sline is None:
        print('Name not found. Returning to menu.')
        return
    if lines[sline][4]:
        print(lines[sline][4])
    else:
        print(f"{sname} doesnt know any commands yet.")
    writer = csv.writer(open('data.csv', 'w', encoding='UTF8', newline=''))
    writer.writerows(lines)

    # To check Counter value call : print(c.count)
