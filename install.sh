#!/usr/bin/env bash
#
# install.sh
#
# install PiTaxiMeter as a service under systemd control
# 
# by Darren Dunford
#

# script control variables
appdir="/opt/pitaximeter"

# update package manager
apt-get update

# install required modules
apt-get install -y python3 python3-pip
pip3 install gpiozero

# create directory structure for app and webapp
mkdir -p $appdir
chgrp -R pi $appdir

# copy webapp and wsgi files
cp pitaximeter.py $appdir

# install service file
cp pitaximeter.service /lib/systemd/system
chmod 644 /lib/systemd/system/pitaximeter.service

# restart Apache and xmastrain service
systemctl daemon-reload
systemctl restart pitaximeter
