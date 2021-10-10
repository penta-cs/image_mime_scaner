

> python -m venv venv

activate venv

> pip install -r requirements.txt 

> pip install "uvicorn[standard]"

> uvicorn main:app --reload 

swagger: 127.0.0.1:8000/docs
