
set -o errexit  # exit on error

pip install -r requirements.txt

# Ejecuta las migraciones
python manage.py migrate

# Crea el superusuario automáticamente
# python manage.py shell << END
# from django.contrib.auth import get_user_model

# User = get_user_model()
# if not User.objects.filter(username='amelendez').exists():
#     User.objects.create_superuser('amelendez', 'amelendez@surgepays.com', 'Jodente_03')
# END
