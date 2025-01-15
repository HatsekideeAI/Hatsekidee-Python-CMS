#!/bin/sh

echo "Controleren en aanmaken van noodzakelijke directories..."

# Maak de directories met de juiste permissies
mkdir -p /var/log/letsencrypt /etc/letsencrypt /var/lib/letsencrypt /var/www/letsencrypt

chmod -R 755 /var/log/letsencrypt /etc/letsencrypt /var/lib/letsencrypt /var/www/letsencrypt
chown -R certbot:certbot /var/log/letsencrypt /etc/letsencrypt /var/lib/letsencrypt /var/www/letsencrypt

echo "Setup voltooid."
