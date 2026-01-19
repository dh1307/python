class Book :
    def __init__(self,booklist,):
        self.booklist = booklist

    def show_books(self):
        if not self.booklist :
            print("No Available Books.")
        else:
            print("Available Books..")
            for book in self.booklist :
                print(book,sep='-')
        

class Library :
    def __init__(self,member_name,member_id):
        self.name = member_name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self):
        if self.borrowed_books :
            print("First Return Borrowed Book ..",self.borrowed_books)
            return
        borrow = input("Enter Name Of Book You Want :")

        if borrow in Books.booklist :
            print("Book Borrowed Sucessfully.")
            self.borrowed_books.append(borrow)
            Books.booklist.remove(borrow)
        else :
            print("Book Not Available.")

    def return_book(self) :
        ret = input("Enter Name Of Book WANT To Return :")
        if ret in self.borrowed_books  :
            print("Sucess..")
            self.borrowed_books.remove(ret)
            Books.booklist.append(ret)
        else :
            print("This Book Is Not Borrowed By You ")


Books = Book(booklist = [
    "Atomic Habits",
    "Rich Dad Poor Dad",
    "The Power of Now",
    "The Great Gatsby"
            ])


Member = Library(member_name = "Dharm",member_id = 12)
print(Member,sep="-")

while True :
    try :
        ans = int(input(
        "      ------   \n"
        "           1. Show All Books\n"   
        "           2. Borrow Book\n"
        "           3. Return Book\n"
        "           4. Exit\n"
        "Enter Your Choice: "
    ))


        if ans == 1 :
            Books.show_books()

        elif ans == 2 :
            Member.borrow_book()

        elif ans == 3 :
            Member.return_book()

        elif ans == 4 :
            print("THANK YOU..")
            break

        else :
            print("Enter Valid Option(1-4)..")

    except ValueError:
        print("Enter Numbers Only ")