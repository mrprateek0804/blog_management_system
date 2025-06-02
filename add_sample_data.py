from app import app, db, User, Post

# Create sample data
with app.app_context():
    # Clear existing data (if any)
    db.drop_all()
    db.create_all()
    
    # Create a sample user with proper password hashing
    user1 = User(username='john_doe', email='john@example.com')
    user1.set_password('password123')  # This will hash the password properly
    db.session.add(user1)
    db.session.commit()
    
    # Create sample posts
    post1 = Post(
        title='My First Blog Post',
        content='This is my very first blog post. I am excited to share my thoughts with the world! Welcome to my amazing blog where I will share all my experiences and learning journey.',
        user_id=user1.id
    )
    
    post2 = Post(
        title='Learning Python Flask',
        content='Today I learned how to create web applications using Python Flask. It is amazing how easy it is to get started! Flask makes web development so much simpler and more enjoyable.',
        user_id=user1.id
    )
    
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
    
    print("Sample data added successfully!")
    print("You can login with:")
    print("Username: john_doe")
    print("Password: password123")