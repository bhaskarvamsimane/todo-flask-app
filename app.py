from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    active_tasks = [task for task in tasks if not task['done']]
    completed_tasks = [task for task in tasks if task['done']]
    return render_template('index.html', active_tasks=active_tasks, completed_tasks=completed_tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    if task:
        tasks.append({'task': task, 'done': False})
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')
