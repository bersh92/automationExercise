# Introduction to Programming with Python - Examples

# This file contains examples of basic Python programming concepts,
# including variables, data types, lists, tuples, and functions.

def demonstrate_variables():
    # Variables and Data Types
    print("\n=== Variables and Data Types ===")
    a_string = "Hello, Python!"
    an_integer = 10
    a_float = 3.14
    a_boolean = True

    print("String:", a_string)
    print("Integer:", an_integer)
    print("Float:", a_float)
    print("Boolean:", a_boolean)


def demonstrate_lists():
    # Lists
    print("\n=== Lists ===")
    a_list = [1, 2, 3, "Python", 3.14]
    print("Original List:", a_list)

    # Adding to a list
    a_list.append("New Element")
    print("After Append:", a_list)

    # Accessing list elements
    print("Second Element:", a_list[1])


def demonstrate_tuples():
    # Tuples
    print("\n=== Tuples ===")
    a_tuple = (1, "Python", 3.14)
    print("Tuple:", a_tuple)

    # Accessing tuple elements
    print("First Element:", a_tuple[0])


def demonstrate_control_flow():
    # Control Flow - if, else
    print("\n=== Control Flow ===")
    number = 10
    if number > 5:
        print("Number is greater than 5")
    else:
        print("Number is 5 or less")

    # for loop with range
    print("For Loop Range(5):")
    for i in range(5):
        print(i)


def demonstrate_functions():
    # Functions
    print("\n=== Functions ===")

    def greet(name):
        return "Hello, " + name + "!"

    greeting = greet("Python Programmer")
    print(greeting)


def main():
    # Main function to execute the examples
    demonstrate_variables()
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_control_flow()
    demonstrate_functions()


if __name__ == "__main__":
    main()
