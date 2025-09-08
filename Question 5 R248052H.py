#Question5 System Flie Handler
from abc import ABC, abstractmethod


# Abstract Base Class
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


# Concrete Class for Text Files
class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                print("\n--- Text File Content ---")
                print(content)
        except FileNotFoundError:
            print("File not found!")

    def write(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)
        print("Data written successfully to text file.")


# Concrete Class for Binary Files
class BinaryFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, 'rb') as file:
                content = file.read()
                print("\n--- Binary File Content (raw bytes) ---")
                print(content)
        except FileNotFoundError:
            print("File not found!")

    def write(self, data):
        with open(self.filename, 'wb') as file:
            file.write(data.encode())  # encoding string to bytes
        print("Data written successfully to binary file.")


# Main Program
def main():
    print("Choose file type handler:")
    print("1. Text File")
    print("2. Binary File")

    choice = input("Enter choice (1/2): ")

    filename = input("Enter filename: ")

    if choice == "1":
        handler = TextFileHandler(filename)
    elif choice == "2":
        handler = BinaryFileHandler(filename)
    else:
        print("Invalid choice!")
        return

    while True:
        print("\nOptions:")
        print("1. Write to file")
        print("2. Read from file")
        print("3. Exit")

        option = input("Enter option (1/2/3): ")

        if option == "1":
            data = input("Enter data to write: ")
            handler.write(data)
        elif option == "2":
            handler.read()
        elif option == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
