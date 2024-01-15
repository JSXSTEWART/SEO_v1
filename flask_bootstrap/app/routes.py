from flask import send_from_directory
from app import app
import os

@app.route('/examples/<path:filename>')
def examples(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'examples'), filename)
