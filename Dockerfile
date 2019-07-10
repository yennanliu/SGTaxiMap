FROM continuumio/miniconda3
ENV PYTHONPATH="$PYTHONPATH:/app"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "run.py"]