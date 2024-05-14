from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    author: Mapped[str] = mapped_column(nullable=False, unique=False)
    rating: Mapped[float] = mapped_column(nullable=False)


class BookForm(FlaskForm):
    book_name = StringField("Book Name", validators=[DataRequired()])
    book_author = StringField("Book Author", validators=[DataRequired()])
    rating = StringField("Rating", validators=[DataRequired()])
    submit = SubmitField("Add Book")


class RatingForm(FlaskForm):
    rating = StringField("New Rating", validators=[DataRequired()])
    submit = SubmitField("Change Rating")


list_books = []


@app.route('/')
def home():
    with app.app_context():

        books = Book.query.all()

    return render_template("index.html", all_books=books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        book = form.book_name.data
        author = form.book_author.data
        rating_book = form.rating.data

        with app.app_context():
            new_book = Book(title=book, author=author, rating=float(rating_book))
            db.session.add(new_book)
            db.session.commit()
        print("True")
        return render_template("book_added.html")
    return render_template("add.html", form=form)


@app.route('/delete/<int:id>')
def erase(id):
    data = Book.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')


@app.route('/rate/<int:id>', methods=['GET', 'POST'])
def change_rating(id):
    form = RatingForm()

    if form.validate_on_submit():
        new_rating = form.rating.data

        with app.app_context():
            book_to_update = db.get_or_404(Book, id)
            book_to_update.rating = float(new_rating)
            db.session.commit()

        return redirect("/")

    data = Book.query.get(id)

    return render_template("new_rate.html", data=data, form=form)


if __name__ == '__main__':
    app.run(debug=True)
