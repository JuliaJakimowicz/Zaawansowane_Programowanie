import csv
import uuid
import os

FILE_NAME = 'zad1_kolejkowanie.csv'

def create_task():
    task_id = str(uuid.uuid4())
    status = 'pending'
    task = {'id': task_id, 'status': status}

    try:
        file_exists = os.path.isfile(FILE_NAME)

        with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'status'])
            if not file_exists:
                writer.writeheader()
            writer.writerow(task)
        print(f"Nowe zadanie dodane: {task}")
    except Exception as e:
        print(f"Błąd podczas zapisywania zadania: {e}")

if __name__ == "__main__":
    create_task()
