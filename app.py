from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

todos = [{"task": "taskname", "done": False}]


@app.route("/")
def index():
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task": todo, "done": False})
    return redirect(url_for("index"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    todo = todos[id]
    if request.method == "POST":
        todo['task'] = request.form['todo']
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, id=id)


@app.route("/check/<int:id>")
def check(id):
    todos[id]['done'] = not todos[id]['done']
    return redirect(url_for("index"))


@app.route("/delete/<int:id>")
def delete(id):
    del todos[id]
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
