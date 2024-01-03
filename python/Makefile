NAME="pyplayground"

up:
	docker compose up -d
down:
	docker compose down -v
exec:
	docker exec -it ${NAME} bash
log:
	docker logs -f ${NAME} --tail=100
