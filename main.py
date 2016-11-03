from flask import Flask, jsonify
from flask import json

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


if __name__ == '__main__':
    app.run(debug=True)
