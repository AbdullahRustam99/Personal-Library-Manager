#  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#               COMMAND-LINE PERSONAL LIBRARY MANAGER
#  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Library = []

def add_book(title, author, year, read):
	if not title or not author or not year:
		print("\nPlease enter a book title, author, and year.\n")
		return
	else:
		read = read.lower() == 'y'
		book = {
			"title": title,
			"author": author,
			"year": int(year),
			"read": read 
		}
		Library.append(book)
		print(f"\nBook '{title}' added to the library.\n")

def remove_book(title):
	if not title:
		print("\nPlease enter a book title.\n")
		return
	else:
		for book in Library:
			if book["title"] == title:
				Library.remove(book)
				print(f"\nBook '{title}' removed from the library.\n")
				return
		print(f"\nBook '{title}' not found in the library.\n")

def display_stats():
	total_books = len(Library)
	print(f"\nTotal Books: {total_books}.")
	read_books = 0
	for books in Library:
		if books['read']:
			read_books += 1
	if total_books > 0:
		read_percentage = (read_books / total_books) * 100
		print(f"\nPercentage of Books Read: {read_percentage}%\n")
	else:
		print("\nPercentage of Books Read: 0%\n")

def book_list():
	if not Library:
		print("\nNo books in the library.\n")
	else:
		for book in Library:
			print(f"\nBOOK NAME: {book['title']}")
			print(f"AUTHOR: {book['author']}")
			print(f"YEAR: {book['year']}\n")		

def find_book(title):
	if not title:
		print("\nPlease enter a book title.\n")
		return
	else:
		for book in Library:
			if book["title"] == title:
				print(f"\nBOOK NAME: {book['title']}")
				print(f"AUTHOR: {book['author']}")
				print(f"YEAR: {book['year']}\n")			
				return
		print(f"\nBook '{title}' not found in the library.\n")

while True:
	print("1. Add Book ")
	print("2. Remove Book ")
	print("3. All Book ")
	print("4. Find Book ")
	print("5. Display statistics")
	print("6. Exit")
	choices = int(input("\nChoose the Option: "))

	if choices == 1:
		title = input("Enter book title: ")
		author = input("Enter book author: ")
		year = input("Enter year of publication: ")
		read = input("Read This Book (y/n): ")
		add_book(title, author, year, read)	
	elif choices == 2:
		title = input("Enter book title to remove: ")
		remove_book(title)	
	elif choices == 3:
		book_list()	
	elif choices == 4:
		title = input("Enter book title to find: ")
		find_book(title)	
	elif choices == 5:
		display_stats()	
	elif choices == 6:	
		print("###########################")
		print("!!!!Good Bye!!!!")
		print("###########################")
		break



