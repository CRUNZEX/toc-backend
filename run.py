from app import app
from app.utils import init

if __name__ == '__main__':
    init()
    app.run(
        host = '0.0.0.0',
        port = 5001,
        debug = True,
    )