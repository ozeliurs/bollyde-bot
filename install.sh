sudo touch /var/discord/bollyde/tmp
sudo rm -r /var/discord/bollyde/*

sudo cp /tmp/bollyde/www/* /var/discord/bollyde/

sudo pip install -r /var/discord/bollyde/requirements.txt

sudo chown -R www-data /var/discord/bollyde/

sudo rm /etc/systemd/system/bollyde-bot.service
sudo cp /tmp/bollyde/bollyde-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl restart bollyde-bot.service

sudo rm -r /tmp/bollyde