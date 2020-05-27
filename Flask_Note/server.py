from flask import Flask, render_template, redirect, request

app = Flask(__name__)

saved_data = {}

# Register the '/' route to this function, this handles the main page: 'http://localhost:5000/'
@app.route('/')
def main_page():  # Just a normal function, I named it this way for cleaner code
    text = None
    # here we use an if statement to see if we have the 'note' key in the dictionary
    if 'note' in saved_data:
        # if yes, we change the None to the saved value in 'text'
        text = saved_data['note']

    # here we use the dictionary's get() method to have 0 when there is no edit_count key
    edits = saved_data.get('edit_count', 0)

    return render_template('index.html', note=text, edit_count=edits)

@app.route('/note', methods=['GET', 'POST'])
def note():
    # when we submit the form with POST method we will have the string 'POST' in request.method
    if request.method == 'POST':
        # we save the new note we got from the POST values
        saved_data['note'] = request.form['note']
        # we update how many times it has been edited
        saved_data['edit_count'] = saved_data.get('edit_count', 0) + 1

        # redirect to the home page which will show the saved note
        return redirect('/')

    return render_template('note.html', note=saved_data.get('note'))

if __name__ == "__main__":
    app.run(
        debug=True, # Allow verbose error reports
        port=5000 # Set custom port
    )