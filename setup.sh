sudo apt-get update
sudo apt-get -y install python-pip
sudo apt-get -y install nginx
sudo apt-get -y install daemontools
sudo service nginx start
git clone https://www.github.com/vsoch/pokemon-server
cd pokemon-server
pip install pokemon

myip="$(dig +short myip.opendns.com @resolver1.opendns.com)"
echo "<h2>telnet ${myip}</h2>" >> index.html
sudo mv index.html /var/www/index.html
supervise $HOME/pokemon-server &
