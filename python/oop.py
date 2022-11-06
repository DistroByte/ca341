# implement a binary search tree

import sys


class Node:
    def __init__(self, name="", number=0, address="", left=None, right=None):
        self.name = name
        self.number = number
        self.address = address
        self.left = left
        self.right = right

    def __str__(self):
        return "Name: " + self.name + "\nNumber: " + str(self.number) + "\nAddress: " + self.address


class NameTree:
    def __init__(self):
        self.root = None

    def insert(self, name, number, address):
        if self.root is None:
            self.root = Node(name, number, address)
        else:
            self._insert(name, number, address, self.root)

    def _insert(self, name, number, address, current):
        if name < current.name:
            if current.left is None:
                current.left = Node(name, number, address)
            else:
                self._insert(name, number, address, current.left)
        elif name > current.name:
            if current.right is None:
                current.right = Node(name, number, address)
            else:
                self._insert(name, number, address, current.right)
        else:
            print("Name already exists in tree")

    def find(self, name):
        if self.root is not None:
            return self._find(name, self.root)
        else:
            return None

    def _find(self, name, current):
        if name == current.name:
            return current
        elif name < current.name and current.left is not None:
            return self._find(name, current.left)
        elif name > current.name and current.right is not None:
            return self._find(name, current.right)

    def delete_tree(self):
        self.root = None

    def delete(self, name):
        if self.root is not None:
            self.root = self._delete(name, self.root)

    def _delete(self, name, current):
        if current is None:
            return current
        if name < current.name:
            current.left = self._delete(name, current.left)
        elif name > current.name:
            current.right = self._delete(name, current.right)
        else:
            if current.left is None and current.right is None:
                current = None
            elif current.left is None:
                current = current.right
            elif current.right is None:
                current = current.left
            else:
                temp = self.get_predecessor(current.left)
                current.name = temp.name
                current.number = temp.number
                current.address = temp.address
                current.left = self._delete(temp.name, current.left)
        return current

    def get_predecessor(self, current):
        if current.right is not None:
            return self.get_predecessor(current.right)
        return current

    def print_tree(self):
        print("--------------------")
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current):
        if current is not None:
            self._print_tree(current.left)
            print("---")
            print(str(current))
            self._print_tree(current.right)


class NumTree:
    def __init__(self):
        self.root = None

    def insert(self, name, number, address):
        if self.root is None:
            self.root = Node(name, number, address)
        else:
            self._insert(name, number, address, self.root)

    def _insert(self, name, number, address, current):
        if number < current.number:
            if current.left is None:
                current.left = Node(name, number, address)
            else:
                self._insert(name, number, address, current.left)
        elif number > current.number:
            if current.right is None:
                current.right = Node(name, number, address)
            else:
                self._insert(name, number, address, current.right)
        else:
            print("Number already exists in tree")

    def find(self, number):
        if self.root is not None:
            return self._find(number, self.root)
        else:
            return None

    def _find(self, number, current):
        if number == current.number:
            return current
        elif number < current.number and current.left is not None:
            return self._find(number, current.left)
        elif number > current.number and current.right is not None:
            return self._find(number, current.right)

    def delete_tree(self):
        self.root = None

    def delete(self, number):
        if self.root is not None:
            self.root = self._delete(number, self.root)

    def _delete(self, number, current):
        if current is None:
            return current
        if number < current.number:
            current.left = self._delete(number, current.left)
        elif number > current.number:
            current.right = self._delete(number, current.right)
        else:
            if current.left is None and current.right is None:
                current = None
            elif current.left is None:
                current = current.right
            elif current.right is None:
                current = current.left
            else:
                temp = self.get_predecessor(current.left)
                current.name = temp.name
                current.number = temp.number
                current.address = temp.address
                current.left = self._delete(temp.name, current.left)
        return current

    def get_predecessor(self, current):
        if current.right is not None:
            return self.get_predecessor(current.right)
        return current

    def print_tree(self):
        print("--------------------")
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current):
        if current is not None:
            self._print_tree(current.left)
            print(str(current))
            self._print_tree(current.right)


def create(name_tree, num_tree):
    print("--------------------")
    name = input("Enter name (leave blank for empty): ")
    number = input("Enter number (leave blank for empty): ")
    address = input("Enter address (leave blank for empty): ")
    name_tree.insert(name, int(number), address)
    num_tree.insert(name, int(number), address)


def find(name_tree, num_tree):
    print("--------------------")
    search = input("Enter search query: ")

    if search.isdigit():
        res = num_tree.find(int(search))
        if res is not None:
            print("Found contact: " + str(res.number) + "\n" + str(res))
        else:
            print("Contact not found")
    else:
        res = name_tree.find(search)
        if res is not None:
            print("Found contact: " + str(res.name) + "\n" + str(res))
        else:
            print("Contact not found")


def delete(name_tree, num_tree):
    print("--------------------")
    search = input("Enter contact information to delete: ")
    if search.isdigit():
        res = num_tree.find(int(search))
        if res is not None:
            print("Deleting contact: " +
                  str(res.number) + "\n" + str(res))
            name_tree.delete(res.name)
            num_tree.delete(res.number)
        else:
            print("Contact not found")
    else:
        res = name_tree.find(search)
        if res is not None:
            print("Deleting contact: " +
                  str(res.name) + "\n" + str(res))
            name_tree.delete(res.name)
            num_tree.delete(res.number)
        else:
            print("Contact not found")


def choices():
    print("--------------------")
    print("1. Create a new contact")
    print("2. Find an existing contact")
    print("3. Delete an existing contact")
    print("4. Print all contacts")
    print("5. Fill with test data")
    print("6. Empty phonebook")
    print("7. Exit program")
    return int(input("Enter choice: "))


def populate(name_tree, num_tree):
    name_tree.insert("Bob", 123, "123 Main St")
    name_tree.insert("John", 456, "456 Main St")
    name_tree.insert("Steve", 789, "789 Main St")
    name_tree.insert("Adam", 111, "111 Main St")
    name_tree.insert("Zach", 222, "222 Main St")
    name_tree.insert("Sam", 333, "333 Main St")
    name_tree.insert("Dave", 444, "444 Main St")
    name_tree.insert("Joe", 555, "555 Main St")
    name_tree.insert("Jack", 666, "666 Main St")
    name_tree.insert("Will", 777, "777 Main St")
    name_tree.insert("Dan", 888, "888 Main St")
    name_tree.insert("Tom", 999, "999 Main St")

    num_tree.insert("Bob", 123, "123 Main St")
    num_tree.insert("John", 456, "456 Main St")
    num_tree.insert("Steve", 789, "789 Main St")
    num_tree.insert("Adam", 111, "111 Main St")
    num_tree.insert("Zach", 222, "222 Main St")
    num_tree.insert("Sam", 333, "333 Main St")
    num_tree.insert("Dave", 444, "444 Main St")
    num_tree.insert("Joe", 555, "555 Main St")
    num_tree.insert("Jack", 666, "666 Main St")
    num_tree.insert("Will", 777, "777 Main St")
    num_tree.insert("Dan", 888, "888 Main St")
    num_tree.insert("Tom", 999, "999 Main St")


if __name__ == "__main__":
    name_tree = NameTree()
    num_tree = NumTree()
    while True:
        choice = choices()
        if choice == 1:
            create(name_tree, num_tree)
            print("Added!")
        elif choice == 2:
            find(name_tree, num_tree)

        elif choice == 3:
            delete(name_tree, num_tree)

        elif choice == 4:
            name_tree.print_tree()

        elif choice == 5:
            print("--------------------")
            populate(name_tree, num_tree)
            print("Test data added")

        elif choice == 6:
            print("--------------------")
            name_tree.delete_tree()
            num_tree.delete_tree()
            print("Phonebook emptied")

        else:
            sys.exit()
