FROM python:3.6

RUN useradd ctf && mkdir -p /app/html && pip install flask

WORKDIR /app

COPY app.py /app/app.py
COPY flag.txt /app/flag.txt
copy html /app/html

RUN chown -R root /app
RUN chmod 555 app.py
RUN chmod 444 flag.txt
RUN chmod 444 html/index.html

USER ctf

CMD python3 app.py
