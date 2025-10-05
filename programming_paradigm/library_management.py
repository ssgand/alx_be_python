class Book:

	def __init__(self, title, author):
		self.title = title
		self.author = author
		self.___is_checked_out = False

	def checkChange(self):
		if self.___is_checked_out == False:
			self.___is_checked_out = True
		elif self.___is_checked_out == True:
			self.___is_checked_out = False

	def get_check(self):
		return self.___is_checked_out

class Library():

	def __init__(self):
		self.___books = []

	def add_book(self, book):
		self.___books.append(book)

	def list_available_books(self):
		for book in self.___books:
			if (book.get_check() == False):
				print(f"{book.title} by {book.author}")

	def check_out_book(self, title):
		for book in self.___books:
			if (book.title == title):
				book.checkChange()

	def return_book(self, title):
		# defining return_book(self)
		for book in self.___books:
			if (book.title == title):
				book.checkChange()
