FROM python:3.7
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip install --upgrade pip && pip install -r requirements.txt 
COPY . /app 
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
