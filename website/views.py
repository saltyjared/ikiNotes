from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# @ represents a function decorator
@views.route('/') # URL route for homepage
def home(): # Called when at route '/'
    return render_template("home.html")