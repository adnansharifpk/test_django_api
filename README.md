# What.AG test_django_api

Instruction to setup and run project on local enviornment
# Clone project
git clone https://github.com/adnansharifpk/test_django_api.git

# Set virtual environment for project
python -m venv venv

#Activate virtual environment
## For windows
venv\Scripts\activate  
## For Linux: 
source venv/bin/activate

# To run project in local environment
python manage.py runserver

# Dockerization (*make sure docker deamon is running in your local machine)
## to build docker container
docker build -t test_django_api .
## to run docker container
docker run -p 8000:8000 product-api
