FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-mar1naRivadeneira.git

WORKDIR /ajedrez-2024-mar1naRivadeneira


RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python -m chess.cli"]

# docker buildx build -t ajedrez-2024-mar1narivadeneira .
# docker run -i ajedrez-2024-mar1narivadeneira