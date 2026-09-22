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

