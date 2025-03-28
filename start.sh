#!/bin/bash
gunicorn -k eventlet -w 1 server:app
chmod +x start.sh