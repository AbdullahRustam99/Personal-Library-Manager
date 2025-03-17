# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#             USING STREAMLIT UI PERSONAL LIBRARY MANAGER
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



import streamlit as st

st.markdown("<h1 class=title> Personal Library Manager</h1>", unsafe_allow_html=True)

if "Library" not in st.session_state:
 	st.session_state.Library = [{ "title": "Harry Potter", "author": "J.K. Rowling", "year": 1997, "read": True},
			      	    { "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937 ,"read": False}, 
				   ]
	 

def add_book(title, author, year,read):
	if not title or not author or not year:
		st.error("Please enter a book title, author, and year.")
		return
	else:
		book = {
			"title": title,
			"author": author,
			"year": year,
			"read": read 
		}
		st.session_state.Library.append(book)
		st.success(f"Book '{title}' added to the library.")


def remove_book(title):
	if not title:
		st.error("Please enter a book title.")
		return
	else:
		for book in st.session_state.Library:
			if book["title"] == title:
				st.session_state.Library.remove(book)
				st.success(f"Book '{title}' removed from the library.")
				return
		st.error(f"Book '{title}' not found in the library.")

def display_stats():
	total_books = len(st.session_state.Library)
	st.markdown(f"Total Books: {total_books}")
	read_books = 0
	for books in st.session_state.Library:
		if books['read'] == True:
			read_books += 1
	if total_books > 0:
		read_percentage = (read_books / total_books) * 100
		st.markdown(f"Percentage of Books Read: {read_percentage}%")
	else:
		st.markdown("Percentage of Books Read: 0%")

def book_list():
	if not st.session_state.Library:
		st.info("No books in the library.")
	else:
		for book in st.session_state.Library:
			st.markdown(f"""
					<div class="book" >
					<p class="bold">BOOK NAME: </p>{book['title']}
					<p class="bold">AUTHOR: </p>{book['author']}
					<p class="bold">YEAR: </p>{book['year']}
					</div>
				""", unsafe_allow_html=True)	

def find_book(title):
	if not title:
		st.error("Please enter a book title.")
		return
	else:
		for book in st.session_state.Library:
			if book["title"] == title:
				st.markdown(f"""
					<div class="book" >
					<p class="bold">BOOK NAME: </p> {book['title']}
					<p class="bold">AUTHOR: </p> {book['author']}
					<p class="bold">YEAR: </p> {book['year']}
					</div>
					</hr>
				""", unsafe_allow_html=True)			
				return
		st.error(f"Book '{title}' not found in the library.")


option = st.radio(" ",("Add Book", "Remove Book", "Display statistics", "All Books", "Find Book"))

if option == "Add Book":
	title = st.text_input("Enter book title:")
	author = st.text_input("Enter book author:")
	year = st.number_input("Enter year of publication:")
	read = st.checkbox("Read Done")
	if st.button("Add Book"):
		add_book(title, author, year,read)

elif option == "Remove Book":
	title = st.text_input("Enter book title to remove:")
	if st.button("Remove Book"):
		remove_book(title)

elif option == "Display statistics":
	display_stats()

elif option == "All Books":
	book_list()

elif option == "Find Book":
	title = st.text_input("Enter book title to find:")
	if st.button("Find Book"):
		find_book(title)

st.markdown("""
<style>
	.title {
		text-align: center;
		font-size: 30px;
		color: #FF5733;
		background:linear-gradient(to right top, #f2ef00, #fccd00, #ffab00, #ff8700, #fb6107);
		border-radius: 10px;
	}
	.st-ag{
	    	flex-direction: row;
	}
	.st-emotion-cache-atejua{
	     	color:#F2FF01;
	     	border-radius: 10px;
	    	font-size: 17px;   
	}
	.st-av {
   	    	background-color: #FF5733;
	}
	.st-bd {
   		background-color: transparent;
	}
	.st-emotion-cache-165fv6u{
	   	color:#F2FF01;
	    	font-size: 17px;
	}
	.book {
           	border: 1px solid #ddd;
            	padding: 10px;
            	margin: 10px 0;
            	border-radius: 5px;
            	background-color: #ffab00;
	    	color:black;
	    
        }
	.bold{
	    	font-weight:bolder; 
	    	font-size:20px;
	    	display: inline;
	    	padding-left:50px;
	    	gap:30px;
	}
	
	
</style>
""", unsafe_allow_html=True)


