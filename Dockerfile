FROM python:3.10.11

WORKDIR /UserManagement 

COPY requirements.txt /UserManagement
COPY . /UserManagement
RUN pip install -r requirements.txt

ENTRYPOINT ["python"] 
CMD ["manage.py", "runserver"]