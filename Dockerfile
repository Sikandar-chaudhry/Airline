FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]