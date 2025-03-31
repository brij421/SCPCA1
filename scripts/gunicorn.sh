#!/usr/bin/bash
sudo cp /mnt/c/SCP/SCPCA1/gunicorn/gunicorn.socket  /etc/systemd/system/gunicorn.socket
sudo cp /mnt/c/SCP/SCPCA1/gunicorn/gunicorn.service  /etc/systemd/system/gunicorn.service

sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service
