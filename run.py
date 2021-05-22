from config import BASE_DIR
from app import app

if __name__ == '__main__':
    print(BASE_DIR)
    app.run(debug=True)
