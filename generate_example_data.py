import sqlite3
import json

# Crear datos de ejemplo para los 4 turnos y 10 empleados por turno
def generate_example_data():
    data = []
    shifts = ["Turno 1", "Turno 2", "Turno 3", "Turno 4"]
    employees = [f"Empleado {i+1}" for i in range(10)]

    task_id = 1
    for shift in shifts:
        for employee in employees:
            task = {
                "id": task_id,
                "title": f"Tarea {task_id}",
                "description": f"Descripción de la tarea {task_id}",
                "status": "Pendiente",
                "shift": shift,
                "assigned_to": employee
            }
            data.append(task)
            task_id += 1

    return data

# Inicializar la base de datos y agregar los datos de ejemplo
def init_db_with_data():
    conn = sqlite3.connect('restaurant_tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, title TEXT, description TEXT, status TEXT, shift TEXT, assigned_to TEXT)''')

    tasks = generate_example_data()
    for task in tasks:
        c.execute('INSERT INTO tasks (title, description, status, shift, assigned_to) VALUES (?, ?, ?, ?, ?)',
                  (task["title"], task["description"], task["status"], task["shift"], task["assigned_to"]))

    conn.commit()
    conn.close()

# Exportar los datos a un archivo JSON
def export_to_json():
    conn = sqlite3.connect('restaurant_tasks.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    tasks = c.execute('SELECT * FROM tasks').fetchall()
    conn.close()

    data = [dict(row) for row in tasks]
    with open('tasks.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    init_db_with_data()
    export_to_json()
