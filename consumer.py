import csv
import time
import os

FILE_NAME = 'zad1_kolejkowanie.csv'

def read_tasks():
    tasks = []
    try:
        if not os.path.exists(FILE_NAME):
            print("Plik z zadaniami nie istnieje. Czekam na nowe zadania...")
            return tasks

        with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            tasks = list(reader)
    except Exception as e:
        print(f"Błąd podczas odczytu pliku: {e}")
    return tasks

def update_task_status(task_id, new_status):
    try:
        tasks = read_tasks()
        updated = False
        for task in tasks:
            if task['id'] == task_id:
                task['status'] = new_status
                updated = True

        if updated:
            with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'status'])
                writer.writeheader()
                writer.writerows(tasks)
        else:
            print(f"Nie znaleziono zadania o ID: {task_id}")
    except Exception as e:
        print(f"Błąd podczas aktualizacji zadania: {e}")

def process_task(task):
    print(f"Rozpoczynam pracę nad zadaniem: {task['id']}")
    update_task_status(task['id'], 'in_progress')
    time.sleep(30)  # Symulacja wykonywania zadania
    print(f"Zadanie zakończone: {task['id']}")
    update_task_status(task['id'], 'done')

def consume_tasks():
    while True:
        tasks = read_tasks()
        pending_tasks = [task for task in tasks if task['status'] == 'pending']

        if pending_tasks:
            for task in pending_tasks:
                process_task(task)
        else:
            print("Brak nowych zadań. Czekam 5 sekund...")
            time.sleep(5)

if __name__ == "__main__":
    consume_tasks()
