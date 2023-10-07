import csv
import os
import os.path
from prettytable import PrettyTable

header = ['Type of animal', 'Animal', 'Name', 'Age', 'Commands']
# data = [{'Domestic', 'Dog', 'Sherkhan', '5', 'Attack'}, {'Pack', 'Horse', 'Moonlight', '10', 'Trot'}]

table = PrettyTable()


# # SearchV()
# selected_date = []  # Creating a list for confirmed notes(rows)
# empty = 'No notes were created on this date.'  # Error messages if no notes(rows) for entered date


# Creating data.csv if it doesn't exist
def Create():
    if os.path.isfile('data.csv') == False:
        with open('data.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(header)


# Append data.csv by adding new note(row)
def AddAnimal():
    r = csv.reader(open('data.csv'))
    # typeof = input('Is it domestic or pack animal? ')
    animal = input('What animal is this? ')
    typeof = ClassifyAnimal(animal)
    name = input('What is the name of this animal? ')
    age = input('How old is this animal? ')
    commands = input('What commands does this animal know? ')
    lines = list(r)
    # animal_id = len(lines) # Через это можно сделать вывод общего кол-ва животных
    row = {'Type of animal': typeof, 'Animal': animal, 'Name': name, 'Age': age, 'Commands': commands}

    # Open the CSV file in "append" mode
    with open('data.csv', 'a', newline='') as f:
        # Create a dictionary writer with the dict keys as column fieldnames
        writer = csv.DictWriter(f, fieldnames=row.keys())

        # Append single row to CSV
        writer.writerow(row)


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


# Function for printing out listed animals
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
# def RemoveAnimal():
#     r = csv.reader(open('data.csv'))
#     lines = list(r)
#     print(lines)
#     e1 = int(input('Enter id: '))
#     lines.pop(e1)
#     writer = csv.writer(open('data.csv', 'w', encoding='UTF8', newline=''))
#     writer.writerows(lines)


# def InputDate():
#     date = input('Enter the date in the format xx.xx.xx or x.xx.xx: ')
#     match = regex.search(date)
#     if match:
#         SearchV(date)
#     else:
#         print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#               "\nWrong format! Pls enter date in the format xx.xx.xx or x.xx.xx"
#               "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#         InputDate()


# def SearchV(date):
#     r = csv.reader(open('data.csv'))
#     lines = list(r)
#     table = PrettyTable()
#     ec = 0
#     for item in list(lines):
#         if date in item:
#             selected_date.append(item)
#             ec += 1
#     if ec != 0:
#         table.add_rows(selected_date)
#         print(table)
#
#     else:
#         print(empty)


# def OneNote():
#     r = csv.reader(open('data.csv'))
#     lines = list(r)
#     table = PrettyTable()
#     on = int(input('Enter note ID to view it: '))
#     print(lines)
#     table.field_names = lines[0]
#     table.add_row(lines[on])
#     print(table)


# Create()
ViewAnimals()
AddAnimal()
# AddCommand()
ViewAnimals()
