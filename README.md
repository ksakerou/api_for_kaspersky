Это мое тестовое задание на стажировку в Kaspersky
IO на моей livecd приказал долго жить, поэтому docker часть
не была протестирована.
Итак, для того, чтобы запустить приложение,в теории необходимо
1) Клонировать репозиторий

git clone https://github.com/ksakerou/api_for_kaspersky.git

2) Собрать docker-образ

docker build . -t myimage

3) Запустить docker-контейнер

docker run -d --name mycontainer -p 80:80 myimage

