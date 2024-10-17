from flask import Flask, request, jsonify

# Initiates the Flask app. (IK)
app = Flask(__name__)

# In-memory storage for both tasks and memories. (IK)
tasks = []
memory = []

# Endpoint to add new tasks (IK)
@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    tasks.append(task)
    return jsonify({"message": "Task Added", "task": task}), 201

# Endpoint that retrieves all tasks (IK)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks}), 200

# Endpoint to add a memory fragment 
@app.route('/memory', methods=['POST'])
def add_memory():
    memory_fragment = request.json. get('memory')
    memory.append(memory_fragment)
    return jsonify({"message": "Memory added", "memory": memory_fragment}), 201

# Endpoint to retrieve all memories
@app.route('/memory', methods=['GET'])
def get_memory():
    return jsonify({"memory": memory}), 200

if __name__ == '__main__':
    app.run(debug=True)

