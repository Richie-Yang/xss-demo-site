from flask import Flask, request, abort, jsonify, render_template, redirect
import webbrowser
import requests
import threading
import os.path
import json
import time
import re
import os
import db
from datetime import datetime

app = Flask(__name__)
return_result = ''


def db_clean():
    try:
        db.delete_comments()
    except Exception:
        pass


@app.route('/', methods=['GET'])
def home():
    return redirect('/index_1')


@app.route('/index_<page_id>', methods=['GET', 'POST'])
def index(page_id):
    global return_result

    if request.method == 'GET':
        try:
            return_result = request.args['query']
            print(return_result)
        except Exception as error:
            print(error)

    elif request.method == 'POST':
        comment = request.form.get('comment')
        current_time = datetime.now().strftime("%B %d, %Y %I:%M%p")
        db.add_comment(comment, current_time)

    comments = db.get_comments()

    return render_template(
        f'index_{page_id}.html',
        return_result=return_result,
        comments=comments,
    )


@app.route('/index_<page_id>/dbclean', methods=['GET'])
def dbclean(page_id):
    db_clean()
    return redirect(f'/index_{page_id}')


@app.after_request
def add_header(response):
    response.cache_control.max_age = 1
    return response


def run_flask_app():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)


if __name__ == "__main__":
    t = threading.Thread(target=run_flask_app)
    t.run()

