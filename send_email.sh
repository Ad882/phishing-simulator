#!/bin/bash

source .env

curl -X POST http://127.0.0.1:5000/send_email \
-H "Content-Type: application/json" \
-d "{\"recipient\": \"$TARGET_EMAIL\"}"