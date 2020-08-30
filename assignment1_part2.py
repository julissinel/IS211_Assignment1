# Create a class called Book. The class should have the following properties:
#a. Two attributes, author and title, both of which should be initialized to the blank string
#b. An __init__ function that takes in an author and a title, and sets them to the object variables

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

# A function called display, which when called, simply prints out a string representing the book
 
    def display(self):
        print('{title}, written by {author}.'.format(title=self.title, author=self.author))


book1 = Book('John Steinbeck', 'Of Mice and Men')
book2 = Book('Harper Lee', 'To Kill a Mockingbird')

book1.display()
book2.display()