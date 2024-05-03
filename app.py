from flask import flask 
app = Flask ( --name--)
@app.route('/')
def hello():
    return 'Hello World, A simple Flask App by Ranjani!!!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
