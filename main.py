import re
import requests

def find_promo_codes(text: str) -> list[str]:
    """
    Находит промокоды в тексте.
    Промокод должен идти после слов 'промокод', 'промо' или 'скидка',
    отделяться пробелом/двоеточием/тире и состоять из 3-15 заглавных букв или цифр.
    """
    
    pattern = r'(?:промокод|промо|скидка)[\s:–—-]+(?-i:([A-Z0-9]{3,15}))\b'
    # Находим слова в любом регистре 
    matches = re.findall(pattern, text, re.IGNORECASE)
    
    # Возвращаем уникальные коды 
    return list(dict.fromkeys(matches))

def get_promos_from_file(filepath: str) -> list[str]:
    """Читает текст из файла и ищет промокоды."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()
        return find_promo_codes(text)
    except FileNotFoundError:
        print(f"Ошибка: Файл {filepath} не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

def get_promos_from_url(url: str) -> list[str]:
    """Скачивает страницу по URL и ищет промокоды в её тексте."""
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return find_promo_codes(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: {e}")
        return []

def main():
    """Главное меню программы."""
    while True:
        print("\n--- ПОИСК ПРОМОКОДОВ ---")
        print("1. Ввести текст вручную")
        print("2. Загрузить из файла (.txt или .html)")
        print("3. Найти на веб-странице (по URL)")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            print("Введите текст (нажмите Enter дважды для завершения):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            text = "\n".join(lines)
            show_result(find_promo_codes(text))

        elif choice == "2":
            filepath = input("Имя файла: ")
            show_result(get_promos_from_file(filepath))

        elif choice == "3":
            url = input("Введите URL (например, https://site.ru): ")
            show_result(get_promos_from_url(url))

        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверная команда.")

def show_result(promos: list[str]):
    """Красивый вывод результатов."""
    if not promos:
        print("Промокоды не найдены.")
    else:
        print(f"Найдено промокодов: {len(promos)}")
        for i, promo in enumerate(promos, 1):
            print(f"  {i}. {promo}")

if __name__ == "__main__":
    main()
