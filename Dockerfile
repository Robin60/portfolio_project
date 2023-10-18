# portfolio_project/Dockerfile

FROM python:3.10.12

WORKDIR /portfolio_project

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

#RUN git clone https://github.com/Robin60/portfolio_project.git .

COPY . /portfolio_project

RUN pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "1-Information_center.py", "--server.port=8501", "--server.address=0.0.0.0"]
