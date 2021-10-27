cd / path / import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

with open('users.json') as f:
    users = json.load(f)


@app.route('/')
def index():
    return render_template("index.html", users=users)


@app.route('/search/')
def search():
    found_users = []
    if request.args.get('name'):
        search_name = request.args.get('name')
        for user in users:
            if search_name in user['name'].lower():
                found_users.append(user)
    return render_template("search.html", users=found_users, found=len(found_users))


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == "GET":
        return render_template("add-user.html", users=users)
    elif request.method == "POST":
        data = request.values
        """new_user = {
           "name":data.get("name"),
           "age":data.get("age"),
           "is_blocked":data.get("is_blocked"),
           "unblock_date":data.get("unblock_date"),
        }"""
        users.append(data)

    with open('users.json', "w") as f:
        f.write(json.dumps(users))

    return redirect("/")


if __name__ == "__main__":
    app.run()