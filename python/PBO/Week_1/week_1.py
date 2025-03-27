# Basic OOP - Week 1

class week1:
    def __init__(self, name : str, age : int) -> None:
        self.name = name 
        self.age = age

    def display(self):
        print(f"Name : {self.name}, Age : {self.age}")

def main():
    testing = week1("Matthew", 20)
    testing.display()

if __name__ == "__main__":
    main()
