from flask import Flask, render_template, url_for
import data_manager

app = Flask('codecool_series')


@app.route('/')
def index():
    result = data_manager.execute_select('SELECT id, title FROM shows;')
    return render_template('index.html', shows=result)


def main():
    app.run()


if __name__ == '__main__':
    main()
