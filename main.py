from flask import Flask, render_template, url_for

app = Flask('codecool_series')


@app.route('/')
def index():
    return render_template('design.html')


def main():
    app.run()


if __name__ == '__main__':
    main()
