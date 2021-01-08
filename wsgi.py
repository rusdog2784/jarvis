import os
from app import create_app


app = create_app()


if __name__ == "__main__":
    PORT = os.getenv("PORT", 5000)
    DEBUG = os.getenv("DEBUG", False)
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
