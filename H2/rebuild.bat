cd InitDB
mysql -u atom --password=atom H2 < rebuild_database.sql
cd ..
python manage.py makemigrations
python manage.py migrate
pause
