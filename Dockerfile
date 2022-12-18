FROM python:3.8

RUN mkdir -p /usr/src/app2/
WORKDIR /usr/src/app2/

COPY . /usr/src/app2/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","main.py"]