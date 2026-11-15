
from flask import jsonify, request
from flaskblog.api import api
from flaskblog.models import Post
from flask_login import login_required, current_user
from flaskblog import db


@api.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)

    post_data = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author.username,
        'user_id': post.user_id,
        'date_posted': post.date_posted.isoformat()
    }

    return jsonify(post_data)


@api.route('/posts', methods=['POST'])
@login_required
def create_post():
    data = request.get_json()
    if not data or not data.get('title') or not data.get('content'):
        return jsonify({'error': 'Title and content are required'}), 400


    post = Post(
        title=data['title'],
        content=data['content'],
        author=current_user
    )

    db.session.add(post)
    db.session.commit()

    return jsonify({
        'message': 'Post created successfully',
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': current_user.username
    }), 201


@api.route('/api/posts/<int:post_id>', methods=['PUT'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        return jsonify({'error': 'Permission denied'}), 403

    data = request.get_json()

    post.title = data['title']
    post.content = data['content']

    db.session.commit()

    return jsonify({
        'message': 'Post updated successfully',
        'id': post.id,
        'title': post.title,
        'content': post.content
    }), 200



@api.route('/posts/<int:post_id>', methods=['DELETE'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        return jsonify({'error': 'Permission denied'}), 403

    db.session.delete(post)
    db.session.commit()

    return jsonify({
        'message': 'Post deleted successfully',
        'id': post_id
    }), 200