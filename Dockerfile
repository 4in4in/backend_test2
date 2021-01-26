FROM python:3.8.5

RUN git clone https://4in4in:sIlVeR1971@github.com/4in4in/backend_test2.git

WORKDIR /backend_test2

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY main.py send_answers.py test_questionnary.json ./

EXPOSE 5006

CMD [ "python3", "main.py" ]
