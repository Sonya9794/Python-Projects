import requests
import time
import os

favorites_path = os.path.join(os.path.dirname(__file__), 'favorite_books.txt')

if not os.path.exists(favorites_path):
    with open(favorites_path, 'x'):
        None


def add_favorite(book):
    request = input("Add this book to your favorites list (Y/N): ").strip().lower()

    if request == 'y':
        with open(favorites_path, 'w') as favorite_books:
            favorite_books.write(f"{book['title']} by {", ".join(book['author_name'])}\n")



requested_api = input("Would you like to search by title, author, or ISBN?: ").strip().lower()

if requested_api == 'title':
    requested_title = input("Enter the title you're looking for: ").strip()
    url = f"https://openlibrary.org/search.json?title={requested_title}"
elif requested_api == 'author':
    requested_author = input("Enter the author you're looking for: ").strip()
    url = f"https://openlibrary.org/search.json?author={requested_author}"
elif requested_api == 'isbn':
    requested_isbn = input("Enter the ISBN number you're looking for: ").strip()
    url = f"https://openlibrary.org/search.json?isbn={requested_isbn}"

query_params = {
    "limit": 5,
    "fields": "title, author_name, first_publish_year,subject"
}

headers = {
    "User-Agent": "Personal practice (singhsonya2008@gmail.com)"
}

response = requests.get(url, headers=headers, params=query_params) #requests the data in json format from the API
data = response.json() #converts response into python dictionary

print("\nHere's what we found!\n")
time.sleep(0.5)

for i, book in enumerate(data["docs"]):
    print("-----------------")
    print(f"{i+1}. Title: {book['title']}\nAuthor: {book['author_name']}")
    time.sleep(0.1)

print("-----------------\n")

selection = int(input("Type a result's number to view more information, or type 0 to exit: ").strip())

if selection-1 not in range(5):
    None
else:
    selection -= 1
    book = data["docs"][selection]
    print(f"\n{selection+1}. Title: {book['title']}\nAuthor:{", ".join(book['author_name'])}\nSubjects: {book['subject'][1]}, {book['subject'][2]}, {book['subject'][3]}\nPublish Year: {book['first_publish_year']}\n")

    add_favorite(book)
    