FROM python:3

RUN pip3 install psutil
COPY ./statistic.py .

CMD python3 /statistic.py
