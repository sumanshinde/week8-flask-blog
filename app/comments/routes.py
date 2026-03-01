from flask import redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.comments import bp
from app.models import Comment

@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    comment = Comment.query.get_or_404(id)
    if comment.author != current_user and comment.post.author != current_user:
        flash('You cannot delete this comment.', 'danger')
        return redirect(url_for('posts.view', id=comment.post.id))
    post_id = comment.post.id
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted.', 'success')
    return redirect(url_for('posts.view', id=post_id))
