#!/bin/bash
# 1. Очистка
echo "Cleaning Jekyll site..."
bundle exec jekyll clean
# 1. Сборка
echo "Building Jekyll site..."
bundle exec jekyll build

# 2. Загрузка с использованием rsync (вместо scp)
# -a: архивный режим (сохраняет права доступа, время и т.д.)
# -v: подробно выводить процесс
# -z: сжимать данные при передаче (экономит трафик)
# --delete: удалять на сервере файлы, которых больше нет у вас (полезно для чистоты)
# --checksum (-c): сверять файлы по содержимому, а не по дате (важно для Jekyll!)

echo "Syncing to 91.188.212.199..."

rsync -avz --checksum --delete -e "ssh -i /c/Users/roman/.ssh/gorbenkoteh2 -p 2222" ./_site/ user@91.188.212.199:/var/www/gorbenkotech/

# 3. Результат
if [ $? -eq 0 ]; then
    echo "Deploy successful!"
else
    echo "Deploy failed!"
fi

read -p "Press Enter to exit"