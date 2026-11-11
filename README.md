# 🐦 Bot Twitter - Buscador de Tweets

API REST construida con **FastAPI** y **Playwright** que busca tweets en X (Twitter) por tema.

## 🚀 Cómo funciona

El bot abre un navegador headless con Playwright, navega a la búsqueda de X/Twitter, y extrae los primeros 5 tweets que coincidan con el tema buscado.

## 📦 Requisitos

- Python 3.10+
- Playwright con Chromium

## ⚙️ Instalación

```bash
pip install -r requirements.txt
playwright install chromium
```

## ▶️ Uso

```bash
python main.py
```

La API se levanta en `http://localhost:8000`. Puedes buscar tweets con:

```
GET /buscar?tema=python
```

### Ejemplo de respuesta

```json
{
  "status": "ok",
  "tema": "python",
  "tweets": [
    "Texto del tweet 1...",
    "Texto del tweet 2..."
  ]
}
```

## 🐳 Docker

```bash
docker build -t bot-twitter .
docker run -p 8000:8000 bot-twitter
```

## 🍪 Cookies (opcional)

Si necesitas cargar cookies de sesión para acceder a contenido restringido, crea un archivo `cookies.json` en la raíz del proyecto. **No subas este archivo a GitHub** (ya está en `.gitignore`).

## 📝 Notas

- El archivo `cookies.json` está excluido del repositorio por seguridad.
- Para Railway, la variable de entorno `PORT` se usa automáticamente.
