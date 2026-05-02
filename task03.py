"""Task 3: Folder Structure Visualization"""

from colorama import Fore
import sys
from pathlib import Path


def print_folder_structure(path: Path, tab_count: int = 0) -> None:
    """
    Print the folder structure of a given directory 
    with color coding (blue for folders, green for files).
    
    :param path: Path to the directory to visualize
    :param tab_count: Indentation level
    """
    tabulation = "  " * tab_count

    if not path.exists():
        print(f"{Fore.RED}Path does not exist: {path}{Fore.RESET}")
        return

    if not path.is_dir():
        print(f"{Fore.RED}Provided path is not a directory: {path}{Fore.RESET}")
        return

    try:
        sorted_elements = sorted(
            path.iterdir(),
            key=lambda p: (not p.is_dir(), p.name)
        )

        for el in sorted_elements:
            if el.is_dir():
                print(f"{tabulation}{Fore.BLUE}{el.name}/{Fore.RESET}")
                print_folder_structure(el, tab_count + 1)
            else:
                print(f"{tabulation}{Fore.GREEN}{el.name}{Fore.RESET}")
    except PermissionError:
        print(f"{Fore.RED}Permission denied: {path}{Fore.RESET}")


def main():
    try:
        directory = Path(sys.argv[1])
    except IndexError:
        directory = Path(__file__).parent
        print(f"{Fore.YELLOW}No path provided. Using: {directory}{Fore.RESET}")

    print_folder_structure(directory)

if __name__ == "__main__":
    main()
