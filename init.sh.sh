#!/bin/bash
echo "🚀 Стартиране на база данни с миграции и seeders..."

docker exec -it laravel_app php artisan migrate:fresh --seed

echo "✅ Базата е готова с роли, акаунти и примерни тулове!"
