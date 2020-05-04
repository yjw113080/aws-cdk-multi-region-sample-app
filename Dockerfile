FROM python:3.7-slim
RUN pip install flask && pip install requests
WORKDIR /app
COPY app.py /app/app.py
ENTRYPOINT ["python"]
CMD ["/app/app.py"]