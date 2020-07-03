from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/animal', methods=['POST'])
def get_text():
    return Response("cow", mimetype='text/plain')

@app.route('/noise', methods=['POST'])
def post_test():
    return Response("moo", mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')
