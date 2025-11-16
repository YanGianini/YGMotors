#!/usr/bin/env bash
set -e

echo "⏳ Aguardando banco de dados em ${DB_HOST}:${DB_PORT}..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "✅ Banco disponível!"

echo "📦 Aplicando migrations..."
alembic upgrade head

echo "🚀 Iniciando API..."
exec "$@"
