FROM python:3.10.6

WORKDIR /Docker_AppFinal

COPY requirements.txt /Docker_AppFinal/requirements.txt 

RUN pip3 install --no-cache-dir --upgrade -r /Docker_AppFinal/requirements.txt  

COPY . /Docker_AppFinal     

CMD bash -c "while true; do sleep1; done"