from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, world! This Flask app is running in a Docker container with CI/CD using GitHub Actions."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # Bind to all interfaces for container networking
