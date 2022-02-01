run:
	uvicorn main:app --reload

d-build:
	docker build -t halfpipe:latest .

d-run: d-stop d-build
	docker run -d -p 8000:8000 -e VERSION=1.0 -e ENVIRON=local halfpipe:latest

d-stop:
	docker stop $$(docker ps -aq) || true && \
	docker rm $$(docker ps -aq) || true