import os
from flask import Flask, render_template, request, url_for, redirect
from google.auth import compute_engine
from google.cloud import firestore

app = Flask(__name__, template_folder='templates')

# Use the default credentials provided by the Cloud Run environment
credentials = compute_engine.Credentials()

# Use these credentials to authenticate with Firestore
db = firestore.Client(credentials=credentials)

todos = db.collection('todos')

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.add({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.stream()
    return render_template('index.html', todos=all_todos)

@app.post('/<id>/delete/')
def delete(id):
    todos.document(id).delete()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)