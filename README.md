# Student1 Game Tracker - XAMPP/MySQL Version

## 1. Start XAMPP
Start **Apache** and **MySQL**.

## 2. Import the database
1. Open `http://localhost/phpmyadmin`
2. Click **Import**
3. Choose this project's `schema.sql`
4. Click **Import / Go**

The SQL file creates the database `game_tracker_db` and its table automatically.

## 3. Install Python packages
```bash
pip install -r requirements.txt
```

## 4. Run Flask
```bash
python app.py
```
Then open `http://127.0.0.1:5000`.

## Database login
The sample uses the normal XAMPP defaults:
- host: localhost
- user: root
- password: empty
- port: 3306

If your MySQL password or port is different, edit `DB_CONFIG` near the top of `app.py`.
