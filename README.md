## Summary
Here I train using Github Actions to automatically test and deploy my project at Yandex Could. <p>
![my badge](https://github.com/KartashevaAnna/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg) </p>

## Description
The project is available through [admin panel](http://84.201.157.9/admin/).
<p> The overall project description is available at https://github.com/KartashevaAnna/api_final_yatube/blob/master/README.md. </p>
This is the link to the same project (without code to deploy it in docker): https://github.com/KartashevaAnna/api_final_yatube.


## Stack
- Python
- Django
- Django REST Framework
- Postgres
- Simple JWT
- Docker
- Gunicorn
- Nginx
- Github actions

## Local deploy
- If you wish to deploy it locally, please, clone it from https://github.com/KartashevaAnna/yamdb_final.
- Create an .env file and fill it with the data to connect to Postgres as required by the settings file.
- Install docker
- Go to yamdb_final\api_yamdb folder.
- Open the command line or git bash and run docker-compose up -d --build
- Then you need to apply migrations: docker-compose exec web python manage.py migrate
- After that you shall collect static: docker-compose exec web python manage.py collectstatic --no-input
- Finally, you create a superuser and access the admin panel: docker-compose exec web python manage.py createsuperuser

## Deploy on a new server
Do the following on the server (in my case it's Yandex Cloud):
- Choose Ubuntu while creating the server
- Run cat ~/.ssh/id_rsa.pub and paste your public key in 'SSH-key' section while creating the server
- For further convenience, make your public ip static (in Virtual Private Cloud section)
- Clone the project from https://github.com/KartashevaAnna/yamdb_final.
- Go to yamdb_final folder, open git bash or command line and connect to the server (ssh name@your-public-ip)
- Run sudo apt update
- Run sudo apt upgrade -y
- Run sudo apt install python3-pip python3-venv git -y
- Generate a pair of ssh keys (while being at your server)
- Run cat ~/.ssh/id_rsa.pub and paste the public key into your Github settings
- Run pip install gunicorn 
- Run sudo systemctl start gunicorn
- Run sudo systemctl enable gunicorn
- Run sudo apt install nginx -y 
- Run sudo ufw allow 'Nginx Full'
- Run sudo ufw allow OpenSSH 
- Run sudo ufw enable
- Run sudo apt install postgresql postgresql-contrib -y
- Run pip install psycopg2-binary==2.8.6 
- Run pip install python-dotenv
- Run sudo apt install docker.io
- Run sudo apt-get update
- Run sudo apt-get install docker-compose-plugin
- Update relevant secrets in Github Actions
- Re-run jobs in Github Actions or push a new version of the code
- Run pip3 install -r /app/requirements.txt --no-cache-dir
- Run sudo docker-compose exec web python manage.py migrate
- Run sudo docker-compose exec web python manage.py createsuperuser
- Run sudo docker-compose exec web python manage.py collectstatic --no-input
- Open local terminal in yamdb_final\api_yamdb\static folder
- RUN scp redoc.yaml name@your-public-ip:/home/name/
- Go back to yamdb_final folder, reconnect to the server
- Run sudo docker cp redoc.yaml CONTAINER_ID:/app/static
- RUN sudo docker exec -it CONTAINER_ID /bin/bash and check whether the file is there (ls, cd static, ls)
- In web browser, go to your-public-ip/admin and your-public-ip/redoc/ to check that the project is available.

### Re-deploy on the existing server
- Re-run jobs in Github Actions or push a new version of the code
- Open local terminal in yamdb_final\api_yamdb\static folder
- RUN scp redoc.yaml name@your-public-ip:/home/name/
- Go back to yamdb_final folder, reconnect to the server
- Run sudo docker cp redoc.yaml CONTAINER_ID:/app/static
- RUN sudo docker exec -it CONTAINER_ID /bin/bash and check whether the file is there (ls, cd static, ls)
- In web browser, go to your-public-ip/admin and your-public-ip/redoc/ to check that the project is available.


