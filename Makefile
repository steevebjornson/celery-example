build:
	docker compose build

up: 
	docker compose up -d 

down:
	docker compose down

run: up
	docker compose run --rm doer /usr/local/bin/python3 -i run.py
