# Инструкция по автоматическому деплою статических сайтов на Google App Engine

## Что должен сделать пользователь

1. **Подготовить файлы сайта**
   - Разместить все html, css, js и изображения в одной папке.
   - Создать файл `app.yaml` (см. пример ниже).

2. **Создать проект в Google Cloud**
   - Перейти в https://console.cloud.google.com/ и создать новый проект.
   - Привязать платёжный аккаунт (если не привязан).

3. **Установить Google Cloud SDK**
   - Скачать и установить Cloud SDK: https://cloud.google.com/sdk/docs/install
   - Войти в аккаунт через команду:
     ```
     gcloud auth login
     ```
   - Выбрать нужный проект:
     ```
     gcloud config set project <PROJECT_ID>
     ```

4. **Создать App Engine приложение**
   - Выполнить команду (указать свой регион, например `europe-central2`):
     ```
     gcloud app create --region=europe-central2
     ```

5. **После выполнения всех технических этапов — уведомить помощника или запустить деплой через помощника.**

---

## Что делает помощник (скрипт/AI)

1. Проверяет наличие всех статических файлов, корректность `app.yaml`, структуру проекта.
2. Назначает необходимые роли сервис-аккаунтам для доступа к Cloud Storage (bucket'ы staging).
3. Активирует необходимые API (`Cloud Build`, `Cloud Storage` и др.) в проекте.
4. Запускает деплой:
   ```
   gcloud app deploy app.yaml
   ```
5. Проверяет результат и выдаёт ссылку на опубликованный сайт.
6. Настраивает дополнительные права, логи, аналитику — по запросу.

---

## Пример файла app.yaml для деплоя статического сайта

```yaml
runtime: python39

handlers:
- url: /
  static_files: index.html
  upload: index.html

- url: /(.*\.(css|js|png|jpg|jpeg|gif|svg))
  static_files: \1
  upload: (.*\.(css|js|png|jpg|jpeg|gif|svg))
```

---

## Ссылки и справка

- [Руководство по деплою (DEPLOY_GUIDE.md)](DEPLOY_GUIDE.md)
- [Google Cloud документация](https://cloud.google.com/appengine/docs)
- [Установка Cloud SDK](https://cloud.google.com/sdk/docs/install)
- [App Engine Regions](https://cloud.google.com/appengine/docs/locations)

---

