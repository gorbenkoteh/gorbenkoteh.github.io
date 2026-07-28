@echo off
:: Запускаем Git Bash, переходим в папку и выполняем скрипт
:: Обратите внимание: путь E:\ превращается в /e/ для Git Bash

start "" "C:\Program Files\Git\git-bash.exe" -c "cd /e/Gorbenkotech.com/gorbenkoteh.github.io_main/docs && sh deploy.sh"