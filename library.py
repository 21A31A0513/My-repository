class book:
    def __init__(self,book_id,title,author,is_available=True):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_available=is_available
    def __str__(self):
        return f"book_id : {self.book_id},Title : {self.title},Author : {self.author},Available : {self.is_available}"
class library:
    def __init__(self):
        self.members=[]
        self.books=[] 
    def add_book(self,book):
        self.books.append(book)
    def remove_book(self,book):
        self.books.remove(book)
    def add_member(self,member):
        self.members.append(member)
    def remove_member(self,member):
        self.members.remove(member)
    def display_books(self):
        for book in self.books:
            print(book)
    def display_members(self):
        for member in self.members:
            print(member)
class member:
    def __init__(self,member_id,name,is_subscribed=False):
        self.member_id=member_id
        self.name=name
        self.is_subscribed=is_subscribed
    def __str__(self):
        return f"member_id : {self.member_id},Name : {self.name},is_subscribed : {self.is_subscribed}"
    def borrow_book(self,book):
        if book.is_available:
            print(f"{self.name} borrowed  {book.title} book") 
            book.is_available=False
        else:
            print(f"sorry!{book.title} book is not available currently")
    def return_book(self,book):
         print(f"{self.name} returned {book.title} book")
         book.is_available=True
#for eg
b1=book(101,"A",'author1')
b2=book(102,"B",'author2',False)
b3=book(103,"C",'author3')
m1=member(1,'member1')
m2=member(2,'member2')
m3=member(3,'member3',True)
l=library()
l.add_book(b1)
l.add_book(b2)
l.add_book(b3)
l.add_member(m1)
l.add_member(m2)
l.add_member(m3)
l.display_books()
l.display_members()
l.remove_book(b2)
l.remove_member(m2)
l.display_books()
l.display_members()
m1.borrow_book(b1)
print(b1)
m2.borrow_book(b1)
m1.return_book(b1)
print(b1)