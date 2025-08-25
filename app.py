from flask import Flask, render_template, request, redirect, url_for, jsonify 
from db import get_db_connection

app = Flask(__name__)

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(64) NOT NULL,
        password VARCHAR(64) NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

init_db()

@app.route("/", methods=["GET","POST"])
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == "POST":
        username = request.form.get("username","anonymous")
        password = request.form.get("password", "")
        content = request.form.get("content","")
        cur.execute(
            "INSERT INTO users (username, password, content) VALUES (%s, %s, %s)",
            (username, password, content)
        )
        conn.commit()

        cur.close()
        conn.close()
        return redirect(url_for("index"))

    cur.execute("SELECT id, username, password, content FROM users ORDER BY id DESC")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", users=users)


if __name__ == "__main__":

    app.run(debug=True)



