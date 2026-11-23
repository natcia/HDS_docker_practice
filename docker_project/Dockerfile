FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt
COPY run_project.py model.joblib test.csv ./
CMD ["python", "run_project.py"]
