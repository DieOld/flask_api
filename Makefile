COMPOSE ?= docker-compose -f docker-compose.yml

build:
	$(COMPOSE) build

run: build
run:
	$(COMPOSE) up -d

logs: build
logs:
	$(COMPOSE) up

remove-compose:
	$(COMPOSE) rm -f