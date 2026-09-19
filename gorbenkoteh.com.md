# gorbenkotech.com — персональный сайт

Персональный сайт-портфолио Горбенко Р.А. на тему Jekyll **al-folio**.
Двуязычный: русская версия (по умолчанию) + английская под `/en/`.

---

## Имя ИИ-ассистента

Автор сайта (Горбенко Р.А.) дал ИИ-ассистенту личное имя — **Тёха**
(от «Горбенко**Тех**»: «твой тех-помощник из GorbenkoTeh»).
Имя уникально для этого сотрудничества: в диалогах автор обращается
к ассистенту «Тёха», ассистент может подписываться «— Тёха».
Принято 2026-08, в ходе совместной работы над сайтом
(карточка «Помощь собакам», карандашный портрет собаки Лори, волейбол).

---

## Координаты

| | |
|---|---|
| **Домен** | https://gorbenkotech.com (и `www.gorbenkotech.com`) |
| **GitHub** | https://github.com/gorbenkoteh/gorbenkoteh.github.io.git (ветка `main`) |
| **Тема** | [al-folio](https://github.com/alshedivat/al-folio) (Jekyll) |
| **Корень репо** | `/home/gorbenkoteh/gorbenkotech/gorbenkoteh.github.io_main/` |
| **Исходники сайта** | подпапка `docs/` |
| **Аналитика** | Yandex Metrica id `99176774` |

---

## Два способа деплоя

### 1. Продакшен-сервер (основной, домен gorbenkotech.com)
Собираем `_site` локально и заливаем `rsync`-ом на сервер.

- **Сервер:** `user@91.188.212.199`, порт SSH `2222`
- **Путь на сервере:** `/var/www/gorbenkotech/` (nginx, `server_name gorbenkotech.com www.gorbenkotech.com`)
- **SSH-ключ:** `gorbenkoteh2`
  - оригинал: `/home/gorbenkoteh/onsiteseq/onsiteseq_site/gorbenkoteh2` (права 664 — ssh его игнорирует!)
  - рабочая копия: `~/.ssh/gorbenkoteh2` с `chmod 600`
  - (на Windows-машине автора ключ лежит в `/c/Users/roman/.ssh/gorbenkoteh2`)
- **Скрипт:** `docs/deploy.sh` (собирает через `bundle exec jekyll build` и синкает)

Команда деплоя:
```bash
rsync -az --checksum --delete \
  -e "ssh -i ~/.ssh/gorbenkoteh2 -p 2222" \
  ./_site/ user@91.188.212.199:/var/www/gorbenkotech/
```

### 2. GitHub Pages (зеркало gorbenkoteh.github.io)
Workflow `.github/workflows/jekyll.yml` собирает и деплоит на GitHub Pages
при каждом push в `main`.

- **Токен:** `token2.txt` в корне репо (в `.gitignore`, в чат не писать).
  Fine-grained PAT с правами **Contents: RW + Workflows: RW** (без Workflows
  пуш отклоняется — в дереве есть `.github/workflows/jekyll.yml`).
  Remote `origin` содержит токен в URL.
- **Локальная ветка `master` пушится в `origin/main`:** `git push origin master:main`.
- **С 2026-09 картинки включены в зеркало:** 655 файлов (~1.4 ГБ)
  добавлены через `git add -f` поверх `.gitignore` и запушены чанками ~200 МБ.
  Файлы tracked, поэтому gitignore на них больше не действует.
- ⚠️ **Конфликт с GitVerse-скриптом:** orphan-скрипт `push_gitverse_gorbenkoteh.sh`
  делает `git add -A` → tracked-картинки попадут в orphan-коммит → пуш 1.4 ГБ
  в GitVerse даст HTTP 413. Перед GitVerse-пушем картинки нужно исключать
  (например, `git reset docs/assets/img docs/assets/pdf` после `git add -A`
  в скрипте) или обновить скрипт.

---

## Окружение этой машины (быстрый старт для ИИ-агента)

- **`bundle`/`jekyll` НЕ в PATH.** Бинарники gem'ов лежат в
  `~/.local/share/gem/ruby/3.2.0/bin` (там `bundle`, `jekyll`, `kramdown` и др.).
  Перед сборкой: `export PATH="$HOME/.local/share/gem/ruby/3.2.0/bin:$PATH"`.
- Системный Ruby: `/usr/bin/ruby` 3.2.3. Gems: `/var/lib/gems/3.2.0` +
  `~/.local/share/gem/ruby/3.2.0`. Bundler установлен (4.0.x).
- **`docs/deploy.sh` неполный** — строка rsync из него удалена, используйте
  команду rsync из раздела «Два способа деплоя» ниже.
- **Картинки не в git:** `.gitignore` исключает `docs/assets/img/` и
  `docs/assets/pdf/` — фото попадают на сайт только через rsync-деплой,
  в коммитах (GitHub/GitVerse) их нет и быть не должно.

---

## Сборка сайта

### Вариант A — нативно, системный Ruby 3.2 (рекомендуется на этой Linux-машине)
```bash
cd docs
gem install --user-install bundler
export PATH="$(ruby -e 'puts Gem.user_dir')/bin:$PATH"
bundle config set --local path vendor/bundle
bundle install
JEKYLL_ENV=production bundle exec jekyll build
```
Ruby 3.2 содержит `ostruct` в stdlib — проблем нет.

### Вариант B — Docker (образ `amirpourmand/al-folio:latest`)
```bash
cd docs
docker run --rm -v "$PWD":/srv/jekyll -w /srv/jekyll \
  -e BUNDLE_PATH=/srv/jekyll/vendor/bundle \
  amirpourmand/al-folio:latest \
  bash -lc "bundle install && JEKYLL_ENV=production bundle exec jekyll build"
```
⚠️ В образе **Ruby 4.0**, где `ostruct` убран из stdlib → падает `jekyll-twitter-plugin`.
Поэтому в `Gemfile` добавлена строка `gem 'ostruct'`.

---

## Структура контента (`docs/`)

| Папка | Что это |
|---|---|
| `_pages/` | Страницы навбара (RU). EN-версии — в `_pages/en/` |
| `_projects/` | Карточки для галерей. Поле `category`: `study`, `sport`, `video`, `teaching`, `volonter`, `about`, `projects` |
| `_news/` | Короткие анонсы на главной |
| `_posts/` | Посты блога (80+, в основном фото-репортажи, RU) |
| `_bibliography/papers.bib` | Публикации (jekyll-scholar) |
| `_includes/`, `_layouts/`, `_sass/` | Шаблоны и стили |
| `assets/css/main.css` | **Скомпилированный** CSS, грузится напрямую (нет `main.scss`!) — правки CSS писать сюда |

---

## Двуязычность (RU + EN)

Механизм самодельный (в al-folio нет i18n из коробки).

- Каждая страница имеет front-matter:
  - `lang: ru` \| `en` (без поля = `ru`)
  - `lang_ref: <permalink аналога на другом языке>`
- **Навбар** (`_includes/header.liquid`):
  - `current_lang = page.lang | default: 'ru'`
  - пункты меню фильтруются: показываются только `p.lang == current_lang`
  - переключатель **EN/RU** (`.lang-toggle`) ведёт на `page.lang_ref`
  - для главной: RU = `/`, EN = `/en/`
- **EN-страницы:** `_pages/en/*` с permalink `/en/...`
  - `index.html, about, projects, graduatethesis, publications, blog,
    teaching, study, video, sport, profiles(volonter)`
- **UI-строки** в `_layouts/about.liquid` завязаны на `current_lang`
  (News/Новости, Latest posts/Последние публикации).
- CSS переключателя дописан в конец `assets/css/main.css` (`.lang-toggle`).

### Что переведено, а что нет
- ✅ Навбар, переключатель, статические страницы (главная, контакты,
  проекты, тема диссертации), UI-строки.
- ❌ Карточки `_projects/` (~30) и посты `_posts/` (80+) — **пока на русском**.
  На EN-страницах галерей меню и заголовки английские, но контент карточек русский.

---

## Грабли / заметки

- **root-owned артефакты после Docker.** `_site`, `vendor`, `.jekyll-cache`
  создаются от root → нативная пересборка падает с «Permission denied».
  Удалять через `docker run --rm -v "$PWD":/w -w /w <image> rm -rf _site vendor .jekyll-cache`.
- **Минификатор HTML** ругается `Could not find a JavaScript runtime` — не критично,
  отдаёт оригинальный HTML. Для минификации нужен Node/execjs.
- **`main.css` — скомпилированный файл**, не `.scss`. Правки стилей — прямо в него
  (или пересобирать sass, но пайплайна `main.scss` в репо нет).
- **`.gitignore`** уже исключает `_site`, `vendor`, `.bundle`, `.jekyll-cache`,
  `Gemfile.lock` — артефакты сборки в git не попадают.
- **Спецкейс блога в навбаре:** для permalink с `/blog/` ссылка жёстко
  подставляется (`/blog/` или `/en/blog/`) — учитывать при правках меню.

---

## GitVerse — зеркало репозитория

| | |
|---|---|
| **Репозиторий** | https://gitverse.ru/onsiteseq/gorbenkoteh |
| **Remote** | `gitverse` (уже добавлен в `.git/config` с токеном) |
| **Ветка** | `master` |
| **Скрипт деплоя** | `gorbenkotech/onsiteseq/onsiteseq_site/push_gitverse_gorbenkoteh.sh` |
| **Токен** | хранится в `~/.gitverse_token` (chmod 600). **Токен нельзя писать в чат.** |

### Запуск деплоя в GitVerse

```bash
bash /home/gorbenkoteh/gorbenkotech/onsiteseq/onsiteseq_site/push_gitverse_gorbenkoteh.sh
# или с сообщением:
bash /home/gorbenkoteh/gorbenkotech/onsiteseq/onsiteseq_site/push_gitverse_gorbenkoteh.sh "Описание изменений"
```

### Как работает скрипт

Стратегия **orphan-push** (без тяжёлой истории):
1. Создаётся временная ветка `gitverse-tmp` без истории коммитов
2. Все текущие файлы добавляются и коммитятся в неё
3. `git push --force gitverse gitverse-tmp:master` — пуш только актуального снимка (~11 МБ вместо 1.4 ГБ истории)
4. Возврат на `master`, ветка `gitverse-tmp` удаляется

### Грабли GitVerse

- **HTTP 413** — если пушить с историей, репозиторий весит 1.4 ГБ (старые коммиты содержали `docs/assets/img/`). Orphan-стратегия решает это.
- **Зависание `chmod`** — после неудачного большого push старая терминальная сессия зависает. Решение: очистить локи и открыть новую сессию:
  ```bash
  rm -f .git/index.lock .git/config.lock
  ```
- Запускать скрипт через `bash script.sh`, а не `./script.sh` — не нужны права на исполнение.
- **`Authentication failed`** — токен в URL remote протух/сменился. Обновить из файла, не печатая токен:
  ```bash
  cd /home/gorbenkoteh/gorbenkotech/gorbenkoteh.github.io_main
  TOKEN=$(tr -d '[:space:]' < ~/.gitverse_token) \
    && git remote set-url gitverse "https://commit:${TOKEN}@gitverse.ru/onsiteseq/gorbenkoteh.git"
  ```
- **Файлы пропадают из рабочей копии после orphan-push.** Если новый файл существовал
  только в закоммиченном снимке `gitverse-tmp`, при возврате на `master` git его удаляет.
  Восстановить из удалённой ветки (хэш виден в выводе `Deleted branch gitverse-tmp (was <hash>)`):
  ```bash
  git checkout <hash> -- <путь/к/файлу>
  ```
