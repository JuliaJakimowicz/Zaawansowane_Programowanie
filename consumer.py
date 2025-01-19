import time

file_path = "tasks.txt"

def process_tasks():
    while True:
        with open(file_path, "r") as file:
            lines = file.readlines()

        tasks = []

        for line in lines:
            task, status = line.strip().split(",")
            tasks.append([task, status])

        task_found = False
        for task in tasks:
            if task[1] == "pending":
                print(f"Rozpoczynam wykonywanie zadania: {task[0]}")
                task[1] = "in_progress"
                task_found = True
                break

        with open(file_path, "w") as file:
            for task in tasks:
                file.write(f"{task[0]},{task[1]}\n")

        if task_found:
            time.sleep(30)

            for task in tasks:
                if task[1] == "in_progress":
                    task[1] = "done"
                    break

            with open(file_path, "w") as file:
                for task in tasks:
                    file.write(f"{task[0]},{task[1]}\n")

            print(f"Zadanie zakończone!")
        else:
            print("Brak zadań do wykonania. Sprawdzam ponownie za 5 sekund.")

        time.sleep(5)

if __name__ == "__main__":
    process_tasks()
