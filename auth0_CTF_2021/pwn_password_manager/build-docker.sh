#!/bin/bash
docker build --tag=password_manager .
docker run -p 1337:1337 --rm --name=password_manager password_manager