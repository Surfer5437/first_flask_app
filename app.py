from flask import Flask, request , render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import choice, randint, sample
app = Flask(__name__)

app.config['SECRET_KEY'] = 'chickensarecool'
debug = DebugToolbarExtension(app)

COMPLIMENTS=['cool','clever', 'tenacious', 'awesome', 'Pythonic']

@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/greet')
def get_greeting():
    username=request.args['username']
    wants=request.args.get('wants_compliments')
    nice_things = sample(COMPLIMENTS, 3)
    return render_template('greet.html', username=username, compliments=nice_things, wants_compliments=wants)

@app.route('/spell/<word>')
def spell_word(word):
    return render_template('spell_word.html', word=word)

@app.route('/lucky')
def lucky_numbner():
    num = randint(1,10)
    return render_template('lucky.html', lucky_num=num)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/hello')
def say_hello():
    return render_template('hello.html')

@app.route('/search')
def search():
    term = request.args['term']
    sort = request.args['sort']
    return f'<h1>Search Results For: {term}</h1><p>Sorted by: {sort}'

# @app.route('/post', methods=['POST'])
# def post_demo():
#     return 'You made a POST request'


@app.route('/add-comment')
def add_comment_form():
    return '''
    <h1>AddComment</h1>
    <form method='POST'>
        <input type='text' placeholder='comment'name='comment'/>
        <input type='text' placeholder='username' name='username'/>
        <button>Submit</button>
    </form>
    '''

@app.route('/add-comment',methods=['POST'])
def save_comment():
    comment= request.form['comment']
    username=request.form['username']
    print(request.form)
    return f'''
    <h1>SAVED YOUR COMMENT!</h1>
    <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment}</li>
    </ul>
    '''

@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f'THIS IS A SUBREDDIT{subreddit}'

POSTS={
    1:'I like chicken tenders',
    2:'I hate Mayo',
    3:'Double rainbow all the way',
    4:'YOLO OMG(kill me)'
}

@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS[id]
    return f'<p>{post}</p>'

@app.route('/r/<subreddit>/comments/<int:post_id>')
def show_comments(subreddit, post_id):
    post = POSTS[post_id]
    return f'<h1>Viewing comments for post with id: {post_id} from {subreddit} Subreddit</h1><br><p>{post}</p>'