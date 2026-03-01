from app import create_app, db
from app.models import User, Post, Comment
from datetime import datetime, timedelta

app = create_app()

with app.app_context():
    # Clear existing data
    db.session.query(Comment).delete()
    db.session.query(Post).delete()
    db.session.query(User).delete()
    db.session.commit()

    # Create users
    u1 = User(username='john', email='john@example.com', about_me='Hi, I am John, a tech enthusiast.')
    u1.set_password('password')
    u2 = User(username='susan', email='susan@example.com', about_me='Hi, I am Susan, a tech enthusiast.')
    u2.set_password('password')
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()

    # Create posts
    p1 = Post(title='Getting Started with Flask Web Development', 
              content='In this comprehensive guide, we will explore how to build your first Flask application. Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.', 
              author=u1,
              timestamp=datetime.utcnow() - timedelta(days=5))
    p2 = Post(title='Python Data Analysis with Pandas', 
              content='Explore data analysis techniques using Python\'s pandas library. Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.', 
              author=u2,
              timestamp=datetime.utcnow() - timedelta(days=2))
    p3 = Post(title='Building REST APIs with Flask', 
              content='A step-by-step guide to creating RESTful APIs. Representational state transfer (REST) is a software architectural style that was created to guide the design and development of the architecture for the World Wide Web.', 
              author=u1,
              timestamp=datetime.utcnow() - timedelta(days=1))
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.commit()

    # Create comments
    c1 = Comment(content='Excellent tutorial! The step-by-step approach really helped me understand Flask better.', author=u2, post=p1)
    c2 = Comment(content='Looking forward to the next part!', author=u1, post=p2)
    c3 = Comment(content='Could you add more examples?', author=u2, post=p3)
    db.session.add(c1)
    db.session.add(c2)
    db.session.add(c3)
    db.session.commit()

    print("Sample data populated successfully.")
