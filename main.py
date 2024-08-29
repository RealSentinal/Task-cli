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

        
        if x == "del":
            with open("data.json", "r") as f:
                data = json.load(f)

            id = int(input("id: "))

            if str(id) in data:
                del data[str(id)]

                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)

            else:
                print("id not found")

        if x == "clear":
            with open("data.json", "w") as f:
                json.dump({}, f)

            print("data cleared")

        if x == "help":
            print("add, list, del, clear, exit, help")

        if x not in ["add", "list", "del", "clear", "exit", "help"]:
            print("command not found")

        if x == "exit":
            break

main()  