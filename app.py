from flask import Flask

app = Flask(__name__)

# Root endpoint that returns 'Hello, World!'
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Health check endpoint for liveness
@app.route('/health')
def health_check():
    return 'Healthy', 200

# Readiness check endpoint for readiness probe
@app.route('/ready')
def readiness_check():
    return 'Ready', 200

if __name__ == '__main__':
    # The app runs on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
