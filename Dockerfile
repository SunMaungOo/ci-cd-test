FROM python:3-slim

COPY ./ ./

ENTRYPOINT [ "python", "main.py" ]