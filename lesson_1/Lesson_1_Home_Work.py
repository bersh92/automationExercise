# Beginner Python Homework: Introduction to Basics

def print_hello_world():
    """Task 1: Print 'Hello, World!' to the console."""
    print("Hello, World!")


def create_and_print_variables():
    """Task 2: Create two variables, `greeting` with any text and `number` with any number, then print both."""
    greeting = "Hello"
    number = 10
    print(greeting + str(number))
    print(greeting)
    print(number)


def sum_two_numbers():
    """Task 3: Create two variables with numbers and print their sum."""
    first_numbers = 13
    second_numbers = 9
    print(first_numbers + second_numbers)


def greet_user():
    """Task 4: Use the input() function to ask the user for their name and greet them."""
    name = input("What is your name?")
    print("Hello, " + name + "!")


def create_list():
    """Task 5: Create a list named `fruits` with any three fruits and print the list."""
    fruits = ["Apple", "Lemon", "Strawberry"]
    print(fruits)


def add_fruit_to_list(fruits):
    """Task 6: Add another fruit to the `fruits` list and print the updated list."""
    fruits = ["Apple", "Lemon", "Strawberry"]
    print("Original List:", fruits)
    fruits.append("Banana")
    print("After Append:", fruits)


def print_fruits(fruits):
    """Task 7: Print each fruit in the `fruits` list using a loop."""
    print("'Apple', 'Lemon', 'Strawberry', 'Banana'")
    for fruits in range(0):
        print(fruits)


def create_and_print_dictionary():
    """Task 8: Create a dictionary named `person` with keys 'name' and 'age', then print the dictionary."""
    person = {'key1': "name", 'key2': "age"}
    print(person)


def update_age_in_dictionary():
    """Task 9: Update the 'age' in the `person` dictionary to a new value and print the updated dictionary."""
    person = {'key1': "name", 'key2': "age"}
    print("Original Dictionary:", person)
    person['key2'] = "new age"
    print("After Updating 'key2':", person)


def check_number_greater_than_10():
    """Task 10: Check if a number stored in a variable is greater than 10 and print a relevant message."""
    number = 15
    if number > 10:
        print("Number is greater than 10")
    else:
        print("Number is 10 or less")


def zapusk_vsech_funkcij_v_etoj():
    print_hello_world()
    create_and_print_variables()
    sum_two_numbers()
    greet_user()
    fruits = create_list()
    add_fruit_to_list(fruits)
    print_fruits(fruits)
    update_age_in_dictionary()
    check_number_greater_than_10()

def zapusk_funkcii_v_kotoroj_zapuskaem_funkcii():
    zapusk_vsech_funkcij_v_etoj()

zapusk_funkcii_v_kotoroj_zapuskaem_funkcii()
