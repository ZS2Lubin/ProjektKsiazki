import json
from pathlib import Path
DB_PATH = Path("books_db.json")
def load_books() -> list[dict]:
    if not DB_PATH.exists():
        return []
    try:
        with DB_PATH.open("r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []
def save_books(books: list[dict]) -> None:
    with DB_PATH.open("w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=2)
def add_book(books: list[dict]) -> None:
    title = input("Podaj tytuł książki: ").strip()
    author = input("Podaj autora: ").strip()
    price_text = input("Podaj cenę (PLN): ").strip()
    if not title or not author:
        print("Tytuł i autor nie mogą być puste.")
        return
    try:
        price = float(price_text)
        if price < 0:
            raise ValueError
    except ValueError:
        print("Niepoprawna cena. Wpisz liczbę większą lub równą 0.")
        return
    books.append({"title": title, "author": author, "price": price})
    save_books(books)
    print("Książka została dodana.")
def list_books(books: list[dict]) -> None:
    if not books:
        print("Brak książek w bazie.")
        return
    print("\n=== Lista książek ===")
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book['title']} - {book['author']} | {book['price']:.2f} PLN")
def seller_panel(books: list[dict]) -> None:
    while True:
        print("\n=== Panel sprzedawcy ===")
        print("1. Wystaw książkę")
        print("2. Zobacz wszystkie książki")
        print("3. Powrót")
        choice = input("Wybierz opcję: ").strip()
        if choice == "1":
            add_book(books)
        elif choice == "2":
            list_books(books)
        elif choice == "3":
            break
        else:
            print("Niepoprawny wybór.")
