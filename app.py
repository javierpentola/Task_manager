from flask import Flask, request, jsonify, send_from_directory, render_template
import sqlite3
import json

app = Flask(__name__, static_folder='static')

def get_db_connection():
    conn = sqlite3.connect('restaurant_tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    with open('tasks.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return jsonify([dict(row) for row in tasks])

# Rutas existentes...
@app.route('/task', methods=['POST'])
def create_task():
    new_task = request.get_json()
    title = new_task['title']
    description = new_task['description']
    status = new_task['status']
    shift = new_task['shift']
    assigned_to = new_task['assigned_to']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (title, description, status, shift, assigned_to) VALUES (?, ?, ?, ?, ?)',
                 (title, description, status, shift, assigned_to))
    conn.commit()
    conn.close()
    
    return jsonify(new_task), 201

@app.route('/task/<int:id>', methods=['PUT'])
def update_task(id):
    updated_task = request.get_json()
    title = updated_task['title']
    description = updated_task['description']
    status = updated_task['status']
    shift = updated_task['shift']
    assigned_to = updated_task['assigned_to']
    
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET title = ?, description = ?, status = ?, shift = ?, assigned_to = ? WHERE id = ?',
                 (title, description, status, shift, assigned_to, id))
    conn.commit()
    conn.close()
    
    return jsonify(updated_task)

@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
