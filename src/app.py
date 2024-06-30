from flask import Flask, jsonify, request



app = Flask(__name__)


todos = [{"label": "Sample", "done": True}]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_todos = jsonify(todos)
    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.remove(todos[position])
    updated_todos = jsonify(todos)
    return updated_todos
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)