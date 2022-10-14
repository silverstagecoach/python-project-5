from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def get_users():
    """Return all users/"""

    return User.query.all()

def get_user_by_id(user_id):
    """Return an individual user"""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def create_movie(title, overview, release_date, poster_path):
    
    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    return movie

def get_movies():
    """Return all movies."""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """Return individual movie"""

    return Movie.query.get(movie_id)

def create_rating(user, movie, score):

    rating = Rating(user=user, movie=movie, score=score)

    return rating

def update_rating(rating_id, new_score):
    """ Update a rating given rating_id and the updated score. """
    rating = Rating.query.get(rating_id)
    rating.score = new_score

if __name__ == '__main__':
    from server import app
    connect_to_db(app)