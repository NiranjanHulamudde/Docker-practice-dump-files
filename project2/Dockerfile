FROM  python:3.9-slim
WORKDIR /app
COPY app/ /app/
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
VOLUME ["/data"]
ENTRYPOINT ["python", "tasks.py"]
CMD ["list"]

