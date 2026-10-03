from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

DB_CONFIG = {
    "host": "sql12.freesqldatabase.com",
    "user": "sql12838220",
    "password": "5dDr4pAi5I",  # XAMPP default is usually empty
    "database": "sql12838220",
    "port": 3306,
    "cursorclass": pymysql.cursors.DictCursor
}

def get_db():
    return pymysql.connect(**DB_CONFIG)

@app.route('/')
def index():
    conn = get_db()
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM games ORDER BY id DESC')
        games = cursor.fetchall()
    conn.close()
    return render_template('index.html', games=games)

@app.route('/add', methods=['POST'])
def add_game():
    title = request.form['title'].strip()
    genre = request.form['genre'].strip()
    rating = request.form['rating']

    if title and genre and rating:
        conn = get_db()
        with conn.cursor() as cursor:
            cursor.execute(
                'INSERT INTO games (title, genre, rating) VALUES (%s, %s, %s)',
                (title, genre, int(rating))
            )
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:game_id>', methods=['POST'])
def delete_game(game_id):
    conn = get_db()
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM games WHERE id = %s', (game_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
