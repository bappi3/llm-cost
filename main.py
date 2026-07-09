import json
from pathlib import Path

USAGE_FILE = Path(__file__).parent / "usage.jsonl"

def main():
    cor = 0
    with open(USAGE_FILE) as f:
        for line in f:
            cor = cor + 1    
    print("Total records:", cor)


if __name__ == "__main__":
    main()
