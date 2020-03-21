kill -9 $(ps -ef | grep "flask" | grep -o "[0-9]*" | head -1)
python -m flask run
