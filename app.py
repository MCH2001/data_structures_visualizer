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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/linkedlist')
def linkedlist():
    return render_template('linkedlist.html')

if __name__ == "__main__":
    app.run(debug=True)