import os

file_path = "tasks.txt"

def add_task():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
    else:
        lines = []

    new_task_name = f"zadanie{len(lines) + 1}"

    with open(file_path, "a") as file:
        file.write(f"{new_task_name},pending\n")
    print(f"Dodano nowe zadanie: {new_task_name}")

if __name__ == "__main__":
    add_task()
