# gorbenkotech.com — персональный сайт

<div align="center">

**Персональный сайт-портфолио Горбенко Романа Алексеевича**

[![Сайт](https://img.shields.io/badge/сайт-gorbenkotech.com-blue)](https://gorbenkotech.com)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-gorbenkoteh.github.io-181717?logo=github)](https://github.com/gorbenkoteh/gorbenkoteh.github.io)
[![GitVerse](https://img.shields.io/badge/GitVerse-onsiteseq%2Fgorbenkoteh-orange)](https://gitverse.ru/onsiteseq/gorbenkoteh)
[![Jekyll](https://img.shields.io/badge/Jekyll-al--folio-CC0000?logo=jekyll)](https://github.com/alshedivat/al-folio)

</div>

---

## О сайте

Персональный сайт-портфолио на тему [al-folio](https://github.com/alshedivat/al-folio) (Jekyll).  
**Трёхъязычный**: русская версия (по умолчанию), английская под `/en/` и китайская под `/zh/`.

**Есть рассказы**: [раздел на сайте](https://gorbenkotech.com/shortstories/) с отдельными языковыми версиями, полными текстами и обложками.

| Параметр | Значение |
|---|---|
| **Домен** | https://gorbenkotech.com и `www.gorbenkotech.com` |
| **GitHub** | https://github.com/gorbenkoteh/gorbenkoteh.github.io (ветка `main`) |
| **GitVerse** | https://gitverse.ru/onsiteseq/gorbenkoteh (ветка `master`) |
| **Тема** | [al-folio](https://github.com/alshedivat/al-folio) (Jekyll) |
| **Аналитика** | Yandex Metrica id `99176774` |

---

## Структура репозитория

```
gorbenkoteh.github.io_main/
├── docs/                    # Исходники сайта (Jekyll)
│   ├── _config.yml          # Основной конфиг Jekyll
│   ├── _pages/              # Страницы навбара (RU + EN + ZH)
│   │   ├── en/              # EN-версии страниц (/en/...)
│   │   └── zh/              # ZH-версии страниц (/zh/...)
│   ├── _projects/           # Карточки проектов и рассказов для галерей
│   ├── _news/               # Короткие анонсы на главной
│   ├── _posts/              # Посты блога (80+, фото-репортажи)
│   ├── _bibliography/
│   │   └── papers.bib       # Публикации (jekyll-scholar)
│   ├── _includes/           # Шаблоны (header, footer, ...)
│   ├── _layouts/            # Лейауты страниц
│   ├── _sass/               # Стили (SCSS)
│   ├── assets/
│   │   ├── css/main.css     # Скомпилированный CSS (правки — сюда!)
│   │   ├── js/              # JavaScript
│   │   ├── img/             # Изображения (в .gitignore, локально)
│   │   ├── pdf/             # PDF-файлы (в .gitignore, локально)
│   │   ├── shortstories/    # Тексты, обложки и генераторы обложек рассказов
│   │   └── video/           # Видео-файлы
│   ├── deploy.sh            # Скрипт rsync-деплоя на продакшен-сервер
│   └── _site/               # Собранный сайт (в .gitignore)
├── gorbenkoteh.com.md       # 📋 Файл памяти проекта (для AI-ассистента)
└── .github/
    └── workflows/
        └── jekyll.yml       # GitHub Actions: сборка и деплой на GitHub Pages
```

### Категории карточек (`_projects/`)

| Категория | Описание |
|---|---|
| `projects` | ИТ-проекты |
| `study` | Обучение и курсы |
| `sport` | Спорт |
| `video` | Видеоконтент / YouTube |
| `teaching` | Преподавание |
| `volonter` | Волонтёрство |
| `about` | О себе |
| `shortstories` | Рассказы (RU) |
| `shortstories_en` | Short stories (EN) |
| `shortstories_zh` | 故事 / рассказы (ZH) |

---

## Трёхъязычность (RU + EN + ZH)

Механизм самодельный (в al-folio нет i18n из коробки).

- Каждая страница имеет front-matter `lang: ru` | `en` | `zh` и `lang_ref: <permalink>`
- Навбар (`_includes/header.liquid`) фильтрует пункты по языку
- Переключатель языка (`.lang-toggle`) образует цикл **РУ → EN → 中文 → РУ** через `page.lang_ref`
- EN-страницы: `_pages/en/*` с permalink `/en/...`
- ZH-страницы: `_pages/zh/*` с permalink `/zh/...`

**Что переведено:**
- ✅ Навбар, переключатель, все статические страницы, UI-строки
- ✅ Раздел рассказов и опубликованные переводы рассказов
- ⚠️ Остальные карточки `_projects/` и посты `_posts/` — преимущественно на русском

---

## Рассказы

Раздел доступен на всех трёх языках:

- RU: [gorbenkotech.com/shortstories/](https://gorbenkotech.com/shortstories/)
- EN: [gorbenkotech.com/en/shortstories/](https://gorbenkotech.com/en/shortstories/)
- 中文: [gorbenkotech.com/zh/shortstories/](https://gorbenkotech.com/zh/shortstories/)

Каждая опубликованная языковая версия рассказа — отдельная карточка в `_projects/` со своей обложкой, интро и полным текстом. Исходные TXT, PNG/SVG и генераторы обложек хранятся в `docs/assets/shortstories/`.

---

## Деплой

### 1. Продакшен-сервер `gorbenkotech.com`

Сборка локально → rsync на сервер.

```bash
# Сборка (из папки docs/)
cd docs
JEKYLL_ENV=production bundle exec jekyll build

# Синк на сервер
rsync -az --checksum --delete \
  -e "ssh -i ~/.ssh/gorbenkoteh2 -p 2222" \
  ./_site/ user@91.188.212.199:/var/www/gorbenkotech/
```

Скрипт: `docs/deploy.sh`  
SSH-ключ: `~/.ssh/gorbenkoteh2` (chmod 600)

### 2. GitHub Pages (зеркало `gorbenkoteh.github.io`)

Автоматически при каждом push в `main` через `.github/workflows/jekyll.yml`.

### 3. GitVerse (зеркало)

```bash
bash /home/gorbenkoteh/gorbenkotech/onsiteseq/onsiteseq_site/push_gitverse_gorbenkoteh.sh
```

Скрипт использует orphan-стратегию (без истории) → push ~11 МБ вместо 1.4 ГБ.

---

## Сборка локально

### Вариант A — нативно (Ruby 3.2, рекомендуется)

```bash
cd docs
gem install --user-install bundler
export PATH="$(ruby -e 'puts Gem.user_dir')/bin:$PATH"
bundle config set --local path vendor/bundle
bundle install
JEKYLL_ENV=production bundle exec jekyll build
```

### Вариант B — Docker

```bash
cd docs
docker run --rm -v "$PWD":/srv/jekyll -w /srv/jekyll \
  -e BUNDLE_PATH=/srv/jekyll/vendor/bundle \
  amirpourmand/al-folio:latest \
  bash -lc "bundle install && JEKYLL_ENV=production bundle exec jekyll build"
```

> ⚠️ В Docker-образе Ruby 4.0, где `ostruct` убран из stdlib.  
> В `Gemfile` добавлена строка `gem 'ostruct'` для совместимости.

---

## Важные заметки

- **`assets/css/main.css`** — скомпилированный файл, не `.scss`. Правки CSS писать прямо в него.
- **`assets/img/` и `assets/pdf/`** — в `.gitignore`, хранятся только локально.
- **Root-owned артефакты после Docker** (`_site`, `vendor`) удалять через:
  ```bash
  docker run --rm -v "$PWD":/w -w /w <image> rm -rf _site vendor .jekyll-cache
  ```
- **Файл памяти проекта**: `gorbenkoteh.com.md` в корне репозитория — подробная документация для AI-ассистента.

---

## Основа темы

Сайт построен на теме [al-folio](https://github.com/alshedivat/al-folio) (Jekyll, MIT License).  
Авторы темы: [Maruan Al-Shedivat](https://maruan.alshedivat.com) и [контрибьюторы](https://github.com/alshedivat/al-folio/graphs/contributors).
