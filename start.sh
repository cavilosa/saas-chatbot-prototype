#!/bin/bash
# This script is used by the production server to start the application.
# It uses Gunicorn, a production-ready web server.

# The --bind 0.0.0.0:5000 tells Gunicorn to listen on all network interfaces.
# The 'run:app' tells Gunicorn to look in the 'run.py' file for the 'app' variable.
gunicorn --workers 3 --bind 0.0.0.0:5000 run:app