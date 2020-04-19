#!/bin/bash
sudo apt-get update
sudo apt-get install python3-pip python-dev nginx git libmysqlclient-dev mysql-server -y
sudo apt-get update
sudo systemctl start mysql
sudo systemctl enable mysql
sudo pip3 install virtualenv
git clone https://github.com/piyushagarwal08/Quiz-Mania-Project1_V2.git
cd Quiz-Mania-Project1_V2/QuizMania
virtualenv venv
source venv/bin/activate
pip install django bcrypt django-extensions gunicorn


python3 manage.py collectstatic
sudo cat <<EOF >> /etc/systemd/system/gunicorn.service
[Unit]
Description=gunicorn daemon
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Quiz-Mania-Project1_V2/QuizMania
ExecStart=/home/ubuntu/Quiz-Mania-Project1_V2/QuizMania/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/Quiz-Mania-Project1_V2/QuizMania/QuizMania.sock QuizMania.wsgi:application
[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

sudo cat <<EOF >> /etc/nginx/sites-available/QuizMania
server {
  listen 80;
  server_name $ip;
  location = /favicon.ico { access_log off; log_not_found off; }
  location /static/ {
      root /home/ubuntu/Quiz-Mania-Project1_V2/QuizMania;
  }
  location / {
      include proxy_params;
      proxy_pass http://unix:/home/ubuntu/Quiz-Mania-Project1_V2/QuizMania/QuizMania.sock;
  }
}
EOF

sudo ln -s /etc/nginx/sites-available/QuizMania /etc/nginx/sites-enabled
sudo nginx -t
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart
