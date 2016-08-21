from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/sciences')
def sciences():
    return render_template('sciences.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/photography')
def photography():
    return render_template('photography.html')

if __name__ == "__main__":
    app.run(debug = True)