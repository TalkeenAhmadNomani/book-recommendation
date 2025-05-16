# End-to-End-Book-Recommender-System

## about project

## A content-based book recommendation system using collaborative filtering

Implemented K-Nearest Neighbors (KNN) for suggesting similar books

Used pandas and scikit-learn for data preprocessing and model building

Dataset includes user ratings, book titles, authors, and metadata

Cleaned and transformed data for optimal model performance

Generated similarity matrix based on user preferences

Built interactive frontend using Streamlit

Displays top recommended books based on user input

Hosted and deployed on AWS EC2

Access the project here: http://13.233.31.189:8501



## Workflow

- config.yaml
- entity
- config/configuration.py
- components
- pipeline
- main.py
- app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/TalkeenAhmadNomani/book-recommendation
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n books python=3.10 -y
```

```bash
conda activate books
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


Now run,
```bash
streamlit run app.py
```


# Streamlit app Docker Image Deployment

## 1. Login with your AWS console and launch an EC2 instance
## 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
git clone "your-project"
```

```bash
docker build -t TalkeenAhmadNomani/book:latest . 
```

```bash
docker images -a  
```

```bash
docker run -d -p 8501:8501 TalkeenAhmadNomani/book 
```

```bash
docker ps  
```

```bash
docker stop container_id
```

```bash
docker rm $(docker ps -a -q)
```

```bash
docker login 
```

```bash
docker push TalkeenAhmadNomani/book:latest 
```

```bash
docker rmi TalkeenAhmadNomani/book:latest
```

```bash
docker pull TalkeenAhmadNomani/book
```







