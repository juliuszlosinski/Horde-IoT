#! /bin/bash

echo "1. Updating..."
apt-get update
echo "1. Finished updating!"

echo "2. Installing Docker..."
apt install docker*
echo "2. Finished installing docker!"

echo "3. Starting Docker..."
systemctl start docker
systemctl status docker
echo "4. Docker started!" 