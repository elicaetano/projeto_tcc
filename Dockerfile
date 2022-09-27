FROM python:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
COPY calendario.py /app.py
CMD ["python","app.py"]