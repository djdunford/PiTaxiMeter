#!/usr/bin/env bash
#
# install.sh
#
# install the service
# 
# by Darren Dunford
#

# script control variables
appdir="/opt/xmastrain"

# update package manager
apt-get update

# install required modules
apt-get install -y apache2 libapache2-mod-wsgi-py3 python3-pip
pip3 install bottle AWSIoTPythonSDK gpiozero

# create directory structure for app and webapp
mkdir -p $appdir
chgrp -R pi $appdir

# copy webapp and wsgi files
cp xmastrain.py $appdir

# install service file
cp xmastrain.service /lib/systemd/system
chmod 644 /lib/systemd/system/xmastrain.service

# restart Apache and xmastrain service
systemctl daemon-reload
systemctl restart xmastrain
