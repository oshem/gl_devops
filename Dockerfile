FROM python:3

RUN pip3 install psutil
COPY ./checker.py .

CMD python3 /checker.py
