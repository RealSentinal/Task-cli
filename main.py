import json
import os

if os.path.exists("data.json"):
    pass
else:
    with open("data.json", "w") as f:
        json.dump({}, f)

def main():
    while True:
        x = str(input("command: "))
        if x == "add":
            with open("data.json", "r") as f:
                data = json.load(f)
    
            if data:
                id = int(max(data.keys())) + 1
            else:
                id = 1

            task = input("task: ")
            if task == "exit":
                break

            data[str(id)] = task

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

        if x == "list":
            with open("data.json", "r") as f:
                data = json.load(f)
            for i in data:
                print( str(i) + ": " + data[i])

main()  