cd InitDB
mysql -u atom --password=atom H2 < rebuild_database.sql
cd ..
python3 manage.py makemigrations
python3 manage.py migrate
pause
