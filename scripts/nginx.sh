
#!/usr/bin/bash
# pathe updated
sudo systemctl daemon-reload
sudo rm -f /etc/nginx/sites-enabled/default

sudo cp /home/ubuntu/SCPCA1/nginx/nginx.conf /etc/nginx/sites-available/WeatherPredic
sudo ln -s /etc/nginx/sites-available/WeatherPredic /etc/nginx/sites-enabled/
#sudo ln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled
#sudo nginx -t
sudo gpasswd -a www-data ubuntu
sudo systemctl restart nginx

