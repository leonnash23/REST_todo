from flask import Flask, jsonify
from flask import abort
from flask import json
from flask import make_response
from flask import request

from model.Task import Task
from model.TaskList import TaskList

main_url = '/todo/api/v1.0/'

app = Flask(__name__)

tasks = TaskList()
tasks.addTask(Task(1, "Бла-бла-бла", ",fsfddf", False))
tasks.addTask(Task(2, "Бла-бла-бла", ",fsfddf", False))
tasks.addTask(Task(3, "Бла-бла-бла", ",fsfddf", False))
tasks.addTask(Task(4, "Бла-бла-бла", ",fsfddf", False))
tasks.addTask(Task(5, "Бла-бла-бла", ",fsfddf", False))


@app.route('/')
def index():
    return "Hello, World!"


@app.route(main_url + 'tasks', methods=['GET'])
def get_tasks():
    return json.dumps({'tasks': tasks.getTasks()}, ensure_ascii=False)


@app.route(main_url + 'tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    if task_id < 0 or task_id > tasks.count:
        abort(404)
    return json.dumps({'task': tasks.task_list[task_id].get_dict()}, ensure_ascii=False)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route(main_url + 'tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = Task(tasks.task_list[-1].task_id + 1,
                request.json['title'],
                request.json.get('description', ""),
                False)
    tasks.addTask(task)
    return json.dumps({'task': task.get_dict()}, ensure_ascii=False),201


if __name__ == '__main__':
    app.run(debug=True)
