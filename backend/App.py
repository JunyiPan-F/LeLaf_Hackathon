from flask import Flask , request , abort , redirect , Response ,url_for, jsonify
from flask_login import LoginManager , login_required , UserMixin , login_user, current_user

import os
app = Flask(__name__)

# Configuring the app
app.config['SECRET_KEY'] = 'secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
class Post:
    def __init__(self , content , postId, comments=[],type='all'):
        self.content = content
        self.postId = postId
        self.comments = comments
        self.type = type

class PostsRepository:
    
        def __init__(self):
            self.posts = dict()
            self.identifier = 0
        
        def save_post(self, post):
            self.posts.setdefault(post.postId, post)
        
        def get_post(self, postId):
            return self.posts.get(postId)
        
        def get_posts(self):
            return self.posts
        
        def get_family_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'family':
                    posts.append(post)
            return posts
        
        def get_relationship_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'relationship':
                    posts.append(post)
            return posts
        
        def get_career_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'career':
                    posts.append(post)
            return posts
        
        def get_personal_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'personal':
                    posts.append(post)
            return posts
        
        def get_finance_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'finance':
                    posts.append(post)
            return posts
        
        def get_lafayette_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'lafayette':
                    posts.append(post)
            return posts
        
        def get_northampton_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'northampton':
                    posts.append(post)
            return posts
        
        def get_lehigh_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'lehigh':
                    posts.append(post)
            return posts
        
        def get_moravian_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'moravian':
                    posts.append(post)
            return posts
        
        def get_cedar_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'cedar':
                    posts.append(post)
            return posts
        
        def get_lehigh_carbon_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'lehigh_carbon':
                    posts.append(post) 
            return posts

        def get_kutztown_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'kutztown':
                    posts.append(post)
            return posts
        
        def get_desales_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'desales':
                    posts.append(post)
            return posts
        
        def get_muhlenberg_posts(self, user):
            posts = []
            for post in self.posts.values():
                if post.type == 'muhlenberg':
                    posts.append(post)
            return posts
        
class User(UserMixin):
    def __init__(self , username , password , id , active=True, email=None, posts=[]):
        self.id = id
        self.username = username
        self.password = password
        self.active = active
        self.email = email
        self.posts = []

    def get_id(self):
        return self.id

    def is_active(self):
        return self.active

    def get_auth_token(self):
        return make_secure_token(self.username , key='secret_key')
    
    def get_username(self):
        return self.username
    
    def get_userInfo(self):
        return {
            'username': self.username,
            'id': self.id,
            'active': self.active,
            'email': self.email
        }
    
    def get_posts(self):
        return self.posts
    



class UsersRepository:

    def __init__(self):
        self.users = dict()
        self.users_id_dict = dict()
        self.identifier = 0
    
    def save_user(self, user):
        self.users_id_dict.setdefault(user.id, user)
        self.users.setdefault(user.username, user)
    
    def get_user(self, username):
        return self.users.get(username)
    
    def get_user_by_id(self, userid):
        return self.users_id_dict.get(userid)
    
    def next_index(self):
        self.identifier +=1
        return self.identifier

users_repository = UsersRepository()
posts_repository = PostsRepository()




# routes

# home page
@app.route('/')
# @login_required
def home():
    print('Home...')
    return Response(
        '''
            <h1>Home Page</h1>
        '''
        )

@app.route('/login' , methods=['GET' , 'POST'])
def login():
    print('Login...')
    if request.method == 'POST':

        data = request.get_data()
        print('Data '+ str(data))
        # password = request.get_data('password')
        json_data = request.get_json()

        if json_data:
            username = json_data.get('username')
            password = json_data.get('password')

            print('Username:', username)
            print('Password:', password)
        
        registeredUser = users_repository.get_user(username)
        print('Registered user '+ str(registeredUser))
        print('Users '+ str(users_repository.users))
        print('Register user %s , password %s' % (registeredUser.username, registeredUser.password))
        if registeredUser != None and registeredUser.password == password:
            print('Logged in..')
            login_user(registeredUser)
            return redirect(url_for('home'))
        else:
            return abort(401)
    else:
         return Response('''
            <form action="" method="post">
                <p><input type=text name=username>
                <p><input type=password name=password>
                <p><input type=submit value=Login>
            </form>
        ''')
        # return jsonify({
        #         "method": "post",
        #         "inputs": [
        #             {"type": "text", "name": "username"},
        #             {"type": "password", "name": "password"}
        #         ],
        #         "submit": {"type": "submit", "value": "Login"}
        #     })

@app.route('/signup', methods=['GET','POST'])
def signup():
    print('Signup...')
    json_data = request.get_json()

    if json_data:
        username = json_data.get('username')
        password = json_data.get('password')

        print('Username:', username)
        print('Password:', password)
        
        new_user = User(username,password,users_repository.next_index())
        users_repository.save_user(new_user)
        print('Registered user '+ str(new_user))
        print("username" + new_user.username)
        print("password" + new_user.password)
    else:
        print('No data')
    return Response("Registered Sucessfully")


@app.route('/profile/<userId>')
@login_required
def profile(userId):
    print('Profile...')
    profile = users_repository.get_user_by_id(userId)
    if profile is None:
        return Response('<p>Profile Design</p>')
    else:
        return Response(
        '''
            <h1>Profile Page</h1>
        '''
        )
    

@app.route('/logout')
@login_required
def logout():
    print('Logged out..')


@app.route('/allPosts/<type>', methods=['GET'])
@login_required
def allPosts(type):
    print('All Posts...')
    if request.method == 'GET':
        posts = []
        if type == 'all':
            posts = posts_repository.get_posts()
        elif type == 'family':
            posts = posts_repository.get_family_posts(current_user)
        elif type == 'relationship':
            posts = posts_repository.get_relationship_posts(current_user)
        elif type == 'career':
            posts = posts_repository.get_career_posts(current_user)
        elif type == 'personal':
            posts = posts_repository.get_personal_posts(current_user)
        elif type == 'finance':
            posts = posts_repository.get_finance_posts(current_user)
        elif type == 'lafayette':
            posts = posts_repository.get_lafayette_posts(current_user)
        elif type == 'northampton':
            posts = posts_repository.get_northampton_posts(current_user)
        elif type == 'lehigh':
            posts = posts_repository.get_lehigh_posts(current_user)
        elif type == 'moravian':
            posts = posts_repository.get_moravian_posts(current_user)
        elif type == 'cedar':
            posts = posts_repository.get_cedar_posts(current_user)
        elif type == 'lehigh_carbon':
            posts = posts_repository.get_lehigh_carbon_posts(current_user)
        elif type == 'kutztown':
            posts = posts_repository.get_kutztown_posts(current_user)
        elif type == 'desales':
            posts = posts_repository.get_desales_posts(current_user)
        elif type == 'muhlenberg':
            posts = posts_repository.get_muhlenberg_posts(current_user)
        else:
            return abort(404)
        return jsonify(posts)
    else:
        return abort(404)


@app.route('/addPost/<type>/<postId>', methods=['POST'])
@login_required
def addPost(type):
    print('Post...')
    if request.method == 'POST':
        json_data = request.get_json()
        content = json_data.get('content')
        postId = json_data.get('postId')
        new_post = Post(posts_repository.next_index(), content, postId, type=type)
        posts_repository.save_post(new_post)
        return Response("Post Added Sucessfully")
    else:
        return abort(404)
    
# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')

# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return users_repository.get_user_by_id(userid)

if __name__ == '__main__':
    app.run(host='172.20.10.7', port=3000, debug =True)