from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def home_page():
    html = '''
    <html>
        <body>
            <h1>Home Page</h1>
            <p>Welcome to my simple app!</p>
            <a href='/hello'>Go to hello page</a>
        </body>
    </html>
    '''
    return html

@app.route('/hello')
def say_hello():
    html = '''
    <html>
        <body>
            <h1>Hello!</h1>
            <a href='/'>Go to main page</a>
        </body>
    </html>
    '''
    return html

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