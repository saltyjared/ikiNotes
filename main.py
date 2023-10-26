from website import create_app

app = create_app()

# only runs app from this file
if __name__ == '__main__':
    app.run(debug=True)