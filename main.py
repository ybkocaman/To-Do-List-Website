from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todo_list = []


@app.route('/')
def index():
    return render_template('index.html', tasks=enumerate(todo_list))


@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        todo_list.append(task)
    return redirect(url_for('index'))


@app.route('/edit_task/<int:index>', methods=['GET', 'POST'])
def edit_task(index):
    if request.method == 'POST':
        new_task = request.form.get('new_task')
        if new_task:
            todo_list[index] = new_task
            return redirect(url_for('index'))
    return render_template('edit.html', task=todo_list[index], task_index=index)


@app.route('/delete_task/<int:index>')
def delete_task(index):
    if index < len(todo_list):
        del todo_list[index]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
