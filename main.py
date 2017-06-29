from flask import Flask

app = Flask('codecool_series')


@app.route('/')
def index():
    return "Welcome TV show lover"


def main():
    app.run()


if __name__ == '__main__':
    main()
