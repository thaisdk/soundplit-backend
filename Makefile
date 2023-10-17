ARG := $(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
$(eval $(ARG):;@true)


run:
	python manage.py runserver

migrate:
	python manage.py migrate

startapp:
	python manage.py startapp $(ARG)