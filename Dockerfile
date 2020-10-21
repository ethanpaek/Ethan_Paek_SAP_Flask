FROM python:3.9-alpine
WORKDIR /ethan_paek_sap
ADD . /ethan_paek_sap
RUN pip install -r requirements.txt
CMD ["python","app.py"]