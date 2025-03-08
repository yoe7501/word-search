import sys 
from typing import Dict, List

def main() -> None:
    """Entrypoint fo program run as module"""
    args: Dict[str, str] = read_args()
    results: List[str] = search_file(args["file_path"], args["keyword"])
    print(len(results))

def read_args() -> Dict[str,str]:
    """Check for valid CLI arguments and return them in a dict"""
    if len(sys.argv) != 3:
        print("Usage: python3 -m cli_args [file] [keyword]")
        exit()
    return {
        "file_path": sys.argv[1],
        "keyword": sys.argv[2]
    }

def search_file(file_path: str, keyword: str) -> List[str]:
    """Opens file_path, reads each line, and returns a list of lines containing w/ keyword"""
    matches: List[str] = []
    file_handle = open(file_path, "r", encoding="utf8")
    for line in file_handle:
        if keyword in line:
            matches.append(line)
    file_handle.close()
    return matches


if __name__ == "__main__":
    main()