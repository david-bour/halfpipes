run:
	uvicorn main:app --reload

docker-build:
	docker build -t halfpipe:latest .

docker-run: docker-stop docker-build
	docker run -d -p 8000:8000 -e VERSION=1.0 -e ENVIRON=local halfpipe:latest

docker-stop:
	docker stop $$(docker ps -aq) || true && \
	docker rm $$(docker ps -aq) || true