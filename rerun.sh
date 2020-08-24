#!/bin/sh

docker-compose build
./clean.sh
docker-compose up
