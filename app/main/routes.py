from flask import render_template, request, current_app
from app.main import bp
from app.models import Post, User, Comment
from sqlalchemy import desc

@bp.route('/')
@bp.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(published=True).order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=10, error_out=False)
    return render_template('main/index.html', title='Home', posts=posts.items, pagination=posts)

@bp.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('main/profile.html', user=user, posts=posts)
