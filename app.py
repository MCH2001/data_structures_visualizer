from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/List')
def List():
    return render_template('List.html')

@app.route('/array')
def array():
    return render_template('array.html')

if __name__ == "__main__":
    app.run(debug=True)