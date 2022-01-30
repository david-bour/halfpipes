run:
	uvicorn main:app --reload

docker-build:
	docker build -t halfpipe:latest .

docker-run:
	docker run -d -p 8000:8000 -e VERSION=1.0 halfpipe:latest

docker-stop:
	docker stop $$(docker ps -aq) && \
	docker rm $$(docker ps -aq)