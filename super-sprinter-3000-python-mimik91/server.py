from flask import Flask, render_template, request, redirect, url_for

import data_handler

USER_STORY = 2
ACCEPTANCE_CRITERIA = 3


app = Flask(__name__)
DATA_HEADER=data_handler.DATA_HEADER

def convert_linebreaks_to_br(original_str):
    return ' '.join(original_str.split('<br>'))

#DATA = data_handler.DATA

@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()
    print(user_stories)
    for story in user_stories:
        user_stories[story][USER_STORY] = convert_linebreaks_to_br(user_stories[story][USER_STORY])
        user_stories[story][ACCEPTANCE_CRITERIA] = convert_linebreaks_to_br(user_stories[story][ACCEPTANCE_CRITERIA])
    return render_template('list.html', DATA_HEADER=DATA_HEADER, user_stories=user_stories)

@app.route('/story')
def edit_list():
    user_stories = data_handler.get_all_user_story()
    return render_template('edit.html', user_stories=user_stories, DATA_HEADER=DATA_HEADER, story_id=None, last_id=max(user_stories.keys()))

@app.route('/story/<story_id>')
def edit_data(story_id):
    user_stories = data_handler.get_all_user_story()
    return render_template('edit.html', user_stories=user_stories, DATA_HEADER=DATA_HEADER, story=user_stories[int(story_id)])

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

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
