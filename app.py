

from flask import Flask, render_template
from routes import register_routes  # Assuming register_routes is in routes.py

app = Flask(__name__)

# Register the routes from routes.py
register_routes(app)

# Home route to render the index.html file
@app.route('/')
def home():
    return render_template('index.html')  # Render index.html from the templates folder

if __name__ == "__main__":
    app.run(debug=True)
