from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        from flask_migrate import upgrade
        upgrade()
    app.run(debug=True, port=5173)