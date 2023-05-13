#! /bin/bash

echo "1. Updating..."
apt-get update
echo "1. Finished updating!"

echo "2. Installing prerequisite packages which let apt use packages over HTTPS..."
apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
echo "2. Finished installing prerequisite packages!"

echo "3. Adding GPG key for the Official Docker repository..."
curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
echo "3. Finished adding GPG key!"

echo "4. Updating database with Docker packages from newly added repo..."
apt-get update
echo "4. Finished updating dabase with Docker packages from newly added repo!

echo "5. Make suring about correct installation of the Docker repo..."
apt-cache policy docker-ce
echo "5. Finished!"

echo "6. Installing Docker..."
apt-get install docker-ce
echo "6. Finished installing docker!"

echo "7. Checking status of the Docker..."
systemctl status docker
echo "7. Finished checking status of the Docker!"
