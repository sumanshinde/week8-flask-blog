from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app import db
from app.posts import bp
from app.posts.forms import PostForm
from app.models import Post, Comment
from app.comments.forms import CommentForm

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, 
                    author=current_user, published=form.published.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('posts/create.html', title='New Post', form=form)

@bp.route('/<int:id>', methods=['GET'])
def view(id):
    post = Post.query.get_or_404(id)
    form = CommentForm()
    
    page = request.args.get('page', 1, type=int)
    comments = post.comments.order_by(Comment.timestamp.desc()).paginate(
        page=page, per_page=10, error_out=False)
    return render_template('posts/view.html', title=post.title, post=post, 
                           form=form, comments=comments.items, pagination=comments)

@bp.route('/<int:id>/comment', methods=['POST'])
def comment(id):
    post = Post.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('You must be logged in to comment.', 'danger')
            return redirect(url_for('auth.login'))
        comment = Comment(content=form.content.data, post=post, author=current_user)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been published.', 'success')
        return redirect(url_for('posts.view', id=post.id))
    return redirect(url_for('posts.view', id=post.id))

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    if post.author != current_user:
        flash('You cannot edit this post.', 'danger')
        return redirect(url_for('posts.view', id=post.id))
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.published = form.published.data
        db.session.commit()
        flash('Your changes have been saved.', 'success')
        return redirect(url_for('posts.view', id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.published.data = post.published
    return render_template('posts/edit.html', title='Edit Post', form=form)

@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    post = Post.query.get_or_404(id)
    if post.author != current_user:
        flash('You cannot delete this post.', 'danger')
        return redirect(url_for('posts.view', id=post.id))
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted.', 'success')
    return redirect(url_for('main.index'))
