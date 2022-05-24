# Old Challenge for Data Engineers. This repo is archived as the interview process has changed.

# Stewards: @team-poseidon
https://linear.app/pleo/project/stewards-data-engineer-challenge-3d3054f515cb

# Welcome!
This repository houses the Pleo Data Engineer challenge. It contains a mix of
detective work, ops-like work, programming and big-picture perspective. Your 
answer to the challenge will help us get to know you, and provide a fun context
for subsequent discussion in our interviews :)

We hope you enjoy it!

## Introduction

You've been tasked with taking over a small prototype for an ETL (Extract - Transform - Load)
pipeline, meant to ferry data from some services over into a Data Warehouse. The
original author never finished the prototype, and they unfortunately also left
very little documentation on how the prototype works! Part of this challenge is
detective work, and so we've been intentionally vague in terms of describing 
how it works.

Luckily you're available to help investigate this, what needs doing, and
even to fix it so that it becomes a functional prototype that we can use to 
evaluate the approach! 

## How to submit a solution

When you are done with the below challenge, you have 2 choices:

1. You can zip the solution up and send it by e-mail to the reviewers.
1. You can set it up as a private GitHub repository and invite the reviewers to the repository.

Please do not submit your challenge by creating it as a fork of the repository :)

## The Task

The ETL service (found in the `etl/` folder) is not yet implemented at all. This is your main task:
Implement a Python-based ETL service such that events are successfully propagated from the services that
produce events, and into the PostgreSQL database representing our 'Data Warehouse'. To do this, 
you will also need to set up the table schemas that you want in the Data Warehouse. You can do this 
in the ETL service as part of running it, or anywhere else you feel is appropriate.

- Remember that you are implementing the remaining parts of a _prototype_ -- you do not have to build
something that is fully viable as a production-grade ETL system.

- The project contains a docker-compose based setup (see `docker-compose.yml`), 
which spawns 2 services that produce events (`users`, `cards`) and 1 service 
which is _not currently implemented_ and is meant to process those produced 
events (`etl`). It also spawns a PostgreSQL database that will act as our 
'Data Warehouse' in this challenge, aptly called `dwh` in the compose file.

- It should be clear how to run the project from this README. If you change things 
that would alter what is needed to run the project, remember to update this README 
file to ensure that the steps required to do so are up-to-date. Unchanged, we will
expect to be able to see you have solved the task by simply running `./rerun.sh`.

- You may improve and modify *any* part of the project, as long as the ETL 
service functions to process and move events from sources into a Data Warehouse.

- Please record your gradual progress and thoughts on this task in the 
`PROGRESS.md` file, in whatever way you feel is appropriate, as you work on 
the task. We suggest a format similar to 'thinking aloud'. If you discover
things that you think are poorly implemented in the existing code, and you
don't want to fix them as part of the challenge, feel free to write here
what you'd suggest doing / changing.

- We value well-written git commits at Pleo! Commits are our history that persists
through both changing issue tracking systems and source code locations, and they
help us understand _why_ something was done if we need to roll things back.
This is a good opportunity to show how you'd ideally write and size your commits.

Hints:
1. We suggest opening the `docker-compose.yml` file and tracing backwards into
the `users` and `cards` services Dockerfiles and codebases. You will almost certainly
want to read through their code to understand them, their events, and where they get
stored.

2. You will want to modify the part(s) of the `docker-compose.yml`
file related to the `etl` service.

*Note*: The rest of this `README.md` provides a standard 'project setup guide'
in terms of running the pipeline.

# Requirements

- You must have Docker installed.
- You must have Docker Compose installed.

# Project layout

The project is meant to be run as a docker-compose project, configured by `docker-compose.yml`. It runs
three Python-based services: `etl`, `cards` and `users`, and a 'Data Warehouse' represented by a PostgreSQL
database.

Each service is built as a Docker image. 

The project also contains some basic convenience scripts (`rerun.sh`, `clean.sh`) for iterative development. 

```
data-engineer-challenge
├── Dockerfile
├── rerun.sh
├── clean.sh
├── database.env
├── docker-compose.yml
├── etl
│   ├── Dockerfile
│   ├── src
│   └── wait-for-it.sh
└── users
    └── src
├── cards
│   └── src
```

### Users Service
The Users service will generate events representing the creation of 1000 randomized users, with incremental ids from 0 up. 

### Cards Service
The Cards service will generate events every few seconds, representing either the creation of a new card or the
modification of an existing one. Sometimes it generates 'bad' events that are missing some information.

### ETL Service (TODO)
The `etl` service is meant to process events emitted by the other services
in this project. It is not yet implemented!

Processing an event means to read it, and to insert it into the PostgreSQL
database (our Data Warehouse), in an appropriate format.

# Setup

You don't actually need any dependencies outside of Docker / Docker Compose, if you run the project that way. However,
if you want to do local Python development also -- and perhaps be able to e.g., run `pip install` on new dependencies
you need and then freeze them into the `requirements.txt` file, it's handy to do the following:

1. Install [pyenv](https://github.com/pyenv/pyenv)
1. Install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
1. Create a new Python 3.7.1 virtualenv: `pyenv virtualenv 3.7.1 data-engineer-challenge`
1. Activate the virtualenv: `pyenv activate data-engineer-challenge`

You can also install [direnv](https://direnv.net/). Each service folder contains a `.direnv` file
with some default env variables, useful if you want to run the service outside Docker Compose.

# Running the project

You are recommended to run the project via Docker Compose. To do so, from the root folder you can run `./rerun.sh` which will run a sequence
of commands to: i) build the containers, ii) remove any hanging folders/volumes from the last run, iii) run the containers.

If you want to run one of the services individually, you'll need to be sure to create any folders it expects to exist. You can get
a sense for the expectations by inspecting the `.direnv` file in the services folder, along with the `clean.sh` script. 
Run `direnv allow` and be sure the necessary folders exist, and in the case of the ETL service that you're running PostgreSQL and a database exists with the credentials matching
those in the `.direnv` file. Generally however, you're advised to run the project via Docker Compose.
