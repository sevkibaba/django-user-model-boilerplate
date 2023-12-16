start:
	@docker run -p 5432:5432 --env-file ./.env_dev -v $(PWD)/.docker/postgres:/var/lib/postgresql/data --name pg-vt -d postgres
stop:
	@docker ps -aq | xargs docker stop
	@docker ps -aq | xargs docker rm -v -f
