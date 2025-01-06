from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes
@app.route('/')
def index():
    return render_template('index.html')  # Reference your HTML file here

@app.route('/upload', methods=['POST'])
def upload_content():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        title = request.form.get('title', 'Untitled')
        body = request.form.get('body', 'No content')

        # Simulate saving to database (you can integrate a real database here)
        print(f"Title: {title}")
        print(f"Body: {body}")
        print(f"Image saved at: {os.path.join(app.config['UPLOAD_FOLDER'], filename)}")

        return jsonify({'message': 'Content uploaded successfully', 'filename': filename}), 200
    else:
        return jsonify({'error': 'Invalid file type'}), 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return jsonify({'message': f"Access file at {os.path.join(UPLOAD_FOLDER, filename)}"})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Database Model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(200), nullable=False)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes
@app.route('/')
def index():
    contents = Content.query.all()
    return render_template('index.html', contents=contents)  # Reference your HTML file here

@app.route('/upload', methods=['POST'])
def upload_content():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)

        title = request.form.get('title', 'Untitled')
        body = request.form.get('body', 'No content')

        # Save to database
        new_content = Content(title=title, body=body, image_path=image_path)
        db.session.add(new_content)
        db.session.commit()

        return jsonify({'message': 'Content uploaded successfully', 'filename': filename}), 200
    else:
        return jsonify({'error': 'Invalid file type'}), 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return jsonify({'message': f"Access file at {os.path.join(UPLOAD_FOLDER, filename)}"})

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_content(id):
    content = Content.query.get_or_404(id)
    try:
        os.remove(content.image_path)  # Remove the associated image file
    except FileNotFoundError:
        pass
    db.session.delete(content)
    db.session.commit()
    return jsonify({'message': 'Content deleted successfully'}), 200

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Database Model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(200), nullable=False)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes
@app.route('/')
def index():
    contents = Content.query.all()
    return render_template('index.html', contents=contents)  # Reference your HTML file here

@app.route('/upload', methods=['POST'])
def upload_content():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)

        title = request.form.get('title', 'Untitled')
        body = request.form.get('body', 'No content')

        # Save to database
        new_content = Content(title=title, body=body, image_path=image_path)
        db.session.add(new_content)
        db.session.commit()

        return jsonify({'message': 'Content uploaded successfully', 'filename': filename}), 200
    else:
        return jsonify({'error': 'Invalid file type'}), 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return jsonify({'message': f"Access file at {os.path.join(UPLOAD_FOLDER, filename)}"})

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_content(id):
    content = Content.query.get_or_404(id)
    try:
        os.remove(content.image_path)  # Remove the associated image file
    except FileNotFoundError:
        pass
    db.session.delete(content)
    db.session.commit()
    return jsonify({'message': 'Content deleted successfully'}), 200

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Database Model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(200), nullable=False)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes
@app.route('/')
def index():
    contents = Content.query.all()
    return render_template('index.html', contents=contents)

@app.route('/upload', methods=['POST'])
def upload_content():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)

        title = request.form.get('title', 'Untitled')
        body = request.form.get('body', 'No content')

        new_content = Content(title=title, body=body, image_path=image_path)
        db.session.add(new_content)
        db.session.commit()

        return jsonify({'message': 'Content uploaded successfully', 'filename': filename}), 200
    else:
        return jsonify({'error': 'Invalid file type'}), 400

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_content(id):
    content = Content.query.get_or_404(id)
    try:
        os.remove(content.image_path)
    except FileNotFoundError:
        pass
    db.session.delete(content)
    db.session.commit()
    return jsonify({'message': 'Content deleted successfully'}), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store submitted articles (in-memory for now)
articles = []

@app.route('/')
def home():
    return render_template('index.html', articles=articles)

@app.route('/submit_article', methods=['POST'])
def submit_article():
    if request.method == 'POST':
        article_content = request.form['articleContent']
        articles.append(article_content)
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin

app = Flask(__name__)

app.secret_key = 'your_secret_key_here'

login_manager = LoginManager()
login_manager.init_app(app)

# In-memory database for users (you can use a proper database in production)
users = {"admin": {"password": "admin123"}}  # In real use, use hashed passwords

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id in users else None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('admin'))
        else:
            return "Invalid credentials, please try again."
    return render_template('login.html')

@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

@app.route('/write_article')
@login_required
def write_article():
    return render_template('write_article.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
import os
from flask import request

@app.route('/upload_image', methods=['POST'])
@login_required
def upload_image():
    if 'image' not in request.files:
        return 'No file part'
    
    file = request.files['image']
    if file.filename == '':
        return 'No selected file'
    
    filename = os.path.join('uploads', file.filename)
    file.save(filename)
    
    return f"File uploaded successfully: {filename}"
from werkzeug.security import generate_password_hash, check_password_hash

# Hash the password before storing it
password_hash = generate_password_hash('admin123')

# When checking the password, use check_password_hash
check_password_hash(password_hash, 'admin123')
from flask import Flask, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change to a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Initialize database
with app.app_context():
    db.create_all()

# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data['name']
    email = data['email']
    password = generate_password_hash(data['password'], method='sha256')

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'})

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid email or password'}), 401

    session['user_id'] = user.id
    session['user_name'] = user.name
    return jsonify({'message': 'Login successful', 'name': user.name})

# Logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully'})

# Protect index endpoint
@app.route('/index')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    return jsonify({'message': f'Welcome, {session["user_name"]}'})

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/get-content', methods=['GET'])
def get_content():
    # Example data - Replace with database query
    articles = [
        {'title': 'First Article', 'content': 'This is the first published article.'},
        {'title': 'Second Article', 'content': 'Here is another amazing article.'},
    ]
    images = [
        {'url': '/static/images/image1.jpg', 'alt': 'Beautiful Scenery'},
        {'url': '/static/images/image2.jpg', 'alt': 'Amazing Sunset'},
    ]

    return jsonify({'articles': articles, 'images': images})
@app.route('/admin/upload', methods=['POST'])
def upload_content():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized access'}), 401

    # Logic to handle article/image uploads
    data = request.json
    # Save data to the database...
    return jsonify({'message': 'Content uploaded successfully'})
from flask import Flask, session, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change to your secret key

@app.route('/admin')
def admin():
    if 'user_id' not in session:  # Ensure the user is logged in as admin
        return redirect(url_for('login'))  # Redirect to login if not logged in
    return render_template('admin.html')  # Render the article writing page

if __name__ == '__main__':
    app.run(debug=True)
