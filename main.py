#!/usr/bin/env venv/bin/python

from app import app
from dotenv_read import port, host


if __name__ == "__main__":
    app.run(debug=True, host=host, port=port)