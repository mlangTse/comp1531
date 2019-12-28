#!/bin/sh
echo "var BACKEND_PORT = $1;" > frontend/prebundle/config.js
cd frontend
python3 static.py $2
