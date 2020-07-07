build:
	@docker-compose build

run:
	@docker-compose up -d

stop:
	@docker-compose down

logs:
	@docker-compose logs -f dash
