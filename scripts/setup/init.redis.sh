#!/bin/sh
# ./hatsekidee/docker/redis/init-redis.sh

set -e  # Stop het script bij fouten
set -u  # Fout bij gebruik van ongedefinieerde variabelen

echo "Initializing Redis with custom configurations..."

# Controleer of het wachtwoord is ingesteld
if [ -z "${REDIS_PASSWORD:-}" ]; then
    echo "Error: Redis password not set. Please set the REDIS_PASSWORD environment variable."
    exit 1
fi

# Controleer of de configuratie bestaat
if [ ! -f /usr/local/etc/redis/redis.conf ]; then
    echo "Error: Redis configuration file not found at /usr/local/etc/redis/redis.conf"
    exit 1
fi

# Log een startmelding
echo "Starting Redis server with custom configurations and password protection..."

# Start Redis met de aangepaste configuratie
exec redis-server /usr/local/etc/redis/redis.conf --requirepass "$REDIS_PASSWORD"
