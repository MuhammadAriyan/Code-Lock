import json
import streamlit as st
import pandas as pd

# File to store books
BOOKS_FILE = "library.json"

# Load books from JSON
def load_books():
    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save books to JSON
def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Initialize books
books = load_books()

# Add book function
def add_book():
    title = st.session_state.get("title", "").strip()
    author = st.session_state.get("author", "").strip()
    year = st.session_state.get("year", "").strip()
    genre = st.session_state.get("genre", "").strip()
    read = st.session_state.get("read")
    
    if not all([title, author, year, genre]):
        st.error("All fields are required!")
        return
    
    # Check for duplicates
    if any(b["title"].lower() == title.lower() and b["author"].lower() == author.lower() for b in books):
        st.warning("This book already exists in your library!")
        return
    
    books.append({"title": title, "author": author, "year": year, "genre": genre, "read": read})
    save_books(books)
    st.success("Book added successfully!")
    st.rerun()

# Remove book function
def remove_book():
    title = st.text_input("Enter book title to remove:", key="remove_title").strip()
    if st.button("Remove Book") and title:
        global books
        new_books = [b for b in books if b["title"].lower() != title.lower()]
        if len(new_books) == len(books):
            st.warning("Book not found!")
        else:
            books = new_books
            save_books(books)
            st.success("Book removed successfully!")
            st.rerun()

# Search books function
def search_books():
    term = st.text_input("Search by title or author:", key="search_term").strip().lower()
    if term:
        results = [b for b in books if term in b["title"].lower() or term in b["author"].lower()]
        if results:
            st.write("### Search Results 🔎")
            st.dataframe(pd.DataFrame(results))
        else:
            st.warning("No books found!")

# UI Setup
st.set_page_config(page_title="Personal Library", page_icon="📚", layout="centered")
st.title("📚 Personal Library Manager")

# Display books
df = pd.DataFrame(books) if books else pd.DataFrame(columns=["title", "author", "year", "genre", "read"])
st.dataframe(df)

# User actions
st.subheader("Manage Your Library")
with st.form("add_book_form"):
    st.text_input("Title:", key="title")
    st.text_input("Author:", key="author")
    st.text_input("Year:", key="year")
    st.text_input("Genre:", key="genre")
    st.radio("Read?", ["Yes", "No"], key="read")
    submitted = st.form_submit_button("Submit")
    if submitted:
        add_book()

remove_book()
search_books()

# Library Stats
if books:
    total_books = len(books)
    read_books = sum(1 for b in books if b["read"] == "Yes")
    st.subheader("📊 Library Statistics")
    st.write(f"**Total Books:** {total_books}")
    st.write(f"**Books Read:** {read_books}")
