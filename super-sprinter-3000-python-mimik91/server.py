from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)
DATA_HEADER=data_handler.DATA_HEADER
STATUSES=data_handler.STATUSES

DATA = {1:[1, "Pszczółka Maja", "Z piosenką Zbysza Wodeckkiego", "No", "6789", 3000, "planing"],
        2:[2, "Scooby Doo", "Z Cartoon-Netwoork po angielsku", "Yes", "6789", 3000, "planing"],
        3:[3, "Scooby Doo", "Z Cartoon-Netwoork po angielsku", "Yes", "6789", 3000, "planing"]}

@app.route('/test')
def test():
    user_stories = data_handler.get_all_user_story()

    return render_template('test.html', user_stories=user_stories, DATA_HEADER=DATA_HEADER)

@app.route('/story/<story_id>')
def edit_data(story_id):
    user_stories = data_handler.get_all_user_story()
    return render_template('edit.html', user_stories=user_stories, DATA_HEADER=DATA_HEADER, story=DATA[int(story_id)])

@app.route('/post/<new_id>', methods=['POST'])
def post_data(new_id):
    title=str(request.form.get('title'))
    story_text=request.form.get('story')
    acceptance = request.form.get('acceptance')
    bussines = request.form.get('bussines')
    estimation = request.form.get('estimation')
    status = request.form.get('status')
    new_story=(new_id, title, story_text,acceptance, bussines, estimation, status)
    DATA[int(new_story[0])]=new_story
    return redirect(url_for('route_list'))




@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()
    return render_template('list.html', DATA_HEADER=DATA_HEADER, DATA=DATA)

@app.route('/story')
def edit_list():
    user_stories = data_handler.get_all_user_story()
    return render_template('edit.html', user_stories=user_stories, DATA_HEADER=DATA_HEADER, story_id=None, last_id=max(DATA.keys()))


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
