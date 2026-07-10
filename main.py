import json
from pathlib import Path

USAGE_FILE = Path(__file__).parent / "usage.jsonl"

def main():
    count = 0
    with open(USAGE_FILE) as f:
        for line in f:
            count = count + 1    
    return count


if __name__ == "__main__":
    main()
