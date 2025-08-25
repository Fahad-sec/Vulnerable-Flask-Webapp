# Vulnerable-Flask-Webapp
This is a deiliberately vulnerable web app built for hands on cybersecurity learning. It stores username, password and  txt content against it in a MySQL database and displays credentials on the web page for testing purposes.

## Purpose
- Gain practical undersating of web applications including all aspects(frontend forms -->backend routes   --> database storage).
- Serve as a testing playgroung to practice common attacks like:
- SQLi
- Auth bypass
- Input validation exploits


# Vulnerable-Flask-Webapp/
```
├─ app.py
├─ db.py
├─ requirements.txt
├─ templates/       
│   └─ index.html
└─ static/          
    ├─ style.css
    ├─ script.js
```

## app.py:
The main Flask application. Handles routing, from submissions, and rendering templates. From here user input from the web page form is processed and sent to the database.

## db.py:
Contains the code to connect to rhe MySQL database. Seperating database login makes the app easier to manage.

## requirements.txt:
Lists all the python packages needed for the project.

## templates/index.html:
The HTML template that displays the form for users to submit data in the webapp. Also shows the credentials on the page for testing and learning purposes.

## static/style.css:
Stylesheet for the webpage, dictates how the form and page elements look.

## static/script.js:
Adds a live preview feature for the message textarea in the form. As the user types in the content box, the content is displayed below. This is intentionally unsafe to demo DOM-based XSS vulnerablilites. It's a controlled example of front-end security flaw.

