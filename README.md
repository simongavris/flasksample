This is a sample python flask API.

Run from Dockerhub:

	simongavris/flasksample


Or Localy

Build:

	docker build  -t python-flask .

Run:

	docker run -p 5000:5000 python-flask

Test:

	curl localhost:5000/test

