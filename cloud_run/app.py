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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form.get('content')
        degree = request.form.get('degree')
        todos.add({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = [{'_id': doc.id, **doc.to_dict()} for doc in todos.stream()]
    return render_template('index.html', todos=all_todos)

@app.route('/<id>/delete/', methods=['POST'])
def delete(id):
    todos.document(id).delete()
    return redirect(url_for('index'))