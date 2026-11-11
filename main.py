from fastapi import FastAPI
from playwright.async_api import async_playwright
import json
import os

app = FastAPI()

@app.get("/buscar")
async def buscar(tema: str):
    async with async_playwright() as p:
        # Lanzamos el navegador sin ventana (obligatorio en Railway)
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

        # Cargar cookies si existen
        if os.path.exists("cookies.json"):
            with open("cookies.json", "r") as f:
                cookies = json.load(f)
                await context.add_cookies(cookies)

        page = await context.new_page()
        url = f"https://x.com/search?q={tema}&src=typed_query"
        
        try:
            await page.goto(url, wait_until="networkidle")
            await page.wait_for_selector('article', timeout=15000)
            
            tweets_elements = await page.query_selector_all('article div[data-testid="tweetText"]')
            
            resultados = []
            for t in tweets_elements[:5]:
                texto = await t.inner_text()
                resultados.append(texto)
                
            await browser.close()
            return {"status": "ok", "tema": tema, "tweets": resultados}
        
        except Exception as e:
            await browser.close()
            return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    # Railway usa la variable de entorno PORT
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)