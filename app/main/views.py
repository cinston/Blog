from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user
from . import main
from .forms import UpdateProfile, AddBlog, CommentForm
from ..models import User, Blog, Comment
from .. import db, photos
import requests
import json


# Views
@main.route('/')
def index():
    """
    Function that renders the index.html file
    """
    blogs = Blog.query.all()
    users = User.query.all()
    
    
    title = 'Welcome to blogs!'
    display=requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    print(display)

    return render_template('index.html', title = title, blogs = blogs, users = users,display=display)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    blogs = Blog.query.filter_by(user_id = user.id).all()
    blogs_count = Blog.count_blogs(uname)
    
    return render_template("profile/profile.html", user=user,blogs=blogs,blogs_count=blogs_count)

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/update.html', form = form, user = user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def add_blog():
    form = AddBlog()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        category = form.category.data

        # Updated blog instance
        new_blog = Blog(title=title,description=blog,category=category, user = current_user, upvotes=0,downvotes=0)

        # Save blog method
        new_blog.save_blog()
        return redirect(url_for('.index'))

    title = 'New blog'
    return render_template('new_blog.html',title = title,blog_form=form )

@main.route('/blogs/<category>')
def get_blogs_category(category):

    blogs = Blog.get_blogs(category)

    return render_template("index.html", blogs = blogs)

@main.route('/blog/<int:id>', methods = ['GET','POST'])
def blog(id):
    blog = Blog.get_blog(id)
    posted_date = blog.posted.strftime('%b %d, %Y')

    if request.args.get("upvote"):
        blog.upvotes += 1

        db.session.add(blog)
        db.session.commit()

        return redirect("/blog/{blog_id}".format(blog_id=blog.id))

    elif request.args.get("downvote"):
        blog.downvotes += 1

        db.session.add(blog)
        db.session.commit()

        return redirect("/blog/{blog_id}".format(blog_id=blog.id))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comment(content = comment,user = current_user,blog_id = blog.id)

        new_comment.save_comment()


    comments = Blog.get_comments(blog)

    return render_template("blog.html", blog = blog, comment_form = comment_form, comments = comments, date = posted_date)