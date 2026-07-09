import json


def main():
    a = 0
    with open("usage.jsonl") as f:
        for line in f:
            record = json.loads(line)
            a = a + 1
            # print(record["model"], record["input_tokens"])
    
    print("Total records:", a)


if __name__ == "__main__":
    main()
