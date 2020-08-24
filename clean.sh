#!/bin/sh

### Stop docker and remove any existing volumes
docker-compose rm -f -v
docker volume rm $(docker volume ls | grep data-engineer-challenge | awk '{print $2}')

### Recreate data folder.
rm -rf ./data
mkdir -p data/events/inbox/cards data/events/inbox/users
mkdir -p data/logs/cards data/logs/users
