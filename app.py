from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/download')
def download_file():
    return send_file('path_to_your_cv.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)



