"""
Task 2: Read Cat Information from a file where each line conains: {id},{name},{age}
"""

def get_cats_info(path: str) -> list[dict[str, str]]:
    """
    Read cat information from a file where each line contains: {id},{name},{age}.

    :param path: Path to the cat information file
    :return: List of dictionaries with cat information
    """
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                if not line:
                    continue

                parts = line.split(',')

                if len(parts) != 3:
                    print(f"[Line {line_number}] Invalid format: {line.strip()}")
                    continue

                identifier, name, age = parts

                if not age.isdigit():
                    print(f"[Line {line_number}] Invalid age: {age}")
                    continue

                cats_info.append({
                    'id': identifier, 
                    'name': name, 
                    'age': age
                })
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []

    except OSError as e:
        print(f"I/O error: {e}")
        return []

    return cats_info

def main():
    cats_info = get_cats_info("cats_file.txt")
    for cat in cats_info:
        print(cat)

if __name__ == "__main__":
    main()
