Przed uruchomieniem projektu upewnij się, że masz zainstalowane:

Python (najnowsza wersja)
Django (najnowsza wersja)
Pillow (projekt używa obrazów)

Możesz zainstalować wymagane pakiety używając pip:
pip install django pillow

Przeprowadź migracje bazy danych:

python manage.py makemigrations
python manage.py migrate

Uruchom serwer deweloperski Django:

python manage.py runserver


Otwórz przeglądarkę i przejdź do http://127.0.0.1:8000/ aby zobaczyć działającą stronę.

Aby stworzyc konto administratora, należy: 

-Przejdź do katalogu głównego Twojego projektu Django, gdzie znajduje się plik manage.py.
-Wpisz w terminalu: python manage.py createsuperuser
-Postępuj zgodnie z instrukcjami na ekranie

Trzeba być zalogowanym by dodawać nowe wpisy, admin może usuwać wpisy poprzez kliknięcie "usuń wpis" przy danym wpisie