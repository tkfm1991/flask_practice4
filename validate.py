from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('name_input.html')


@app.route('/validate', methods=['POST'])
def validate():
    name = request.form['name']
    name2 = request.form['name2']

    if name != name2:
        error = '入力内容が一致しません'
        return render_template('name_input.html', error=error)

    return redirect(url_for('success'))


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
