"""
Task 1: Calculate total and average salary from a file where each line conains: {name},{salary}
"""

def total_salary(path: str) -> tuple[int, float]:
    """
    Calculate total and average salary from a file where each line conains: {name},{salary}.

    :param path: Path to the salary file
    :return: Tuple (total_salary, average_salary)
    """
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                user_info = line.strip().split(',')

                if len(user_info) != 2:
                    print(f"[Line {line_number}] Invalid format: {line.strip()}")
                    continue

                try:
                    salary = int(user_info[1])
                except ValueError:
                    print(f"[Line {line_number}] Invalid salary: {user_info[1]}")
                    continue

                total += salary
                count += 1
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0.0

    except OSError as e:
        print(f"I/O error: {e}")
        return 0, 0.0

    average: float = total / count if count > 0 else 0.0

    return total, average


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
