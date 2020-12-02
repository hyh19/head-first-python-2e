
from vsearch import search4letters
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def render_search_response(gen_json:bool=False) -> str:
    """Return either a JSON- or HTML-formatted search response."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    if gen_json:
        return jsonify(the_phrase=phrase,
                       the_letters=letters,
                       the_results=results)
    return render_template('results.html',
                           the_title='Here are your results!',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)

@app.route('/entry')
def entry_page() -> 'html':
    """Returns the entry page to browser."""
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!',
                           the_url='/search4')

@app.route('/search4', methods=['POST'])
def search4() -> 'html':
    """Returns the results of a call to 'search4letters' to the browser."""
    return render_search_response()

@app.route('/entryjson')
def entry_json_page() -> 'html':
    """Returns the JSON entry page to browser."""
    return render_template('entry.html',
                           the_title='Welcome to search4letters JSON page',
                           the_url='/searchjson')

@app.route('/searchjson', methods=['POST'])
def search4json() -> 'json':
    """Returns the results of a call to 'search4letters' to the browser."""
    return render_search_response(True)

if __name__ == '__main__':
    app.run(debug=True)
