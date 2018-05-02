from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def my_microservice():
    return jsonify({'Test' : 'Response'})

if __name__ == '__main__':
    app.run()