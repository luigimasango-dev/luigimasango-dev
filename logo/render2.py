import asyncio
from playwright.async_api import async_playwright
from PIL import Image, ImageDraw
d="C:/Dev/gh-profile/logo/"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":512,"height":512})
        await pg.goto("file:///"+d+"logo.svg"); await pg.screenshot(path=d+"logo.png"); await b.close()
asyncio.run(main())
im=Image.open(d+"logo.png").resize((300,300)); m=Image.new("L",(300,300),0); ImageDraw.Draw(m).ellipse((0,0,299,299),fill=255)
s=Image.new("RGB",(420,320),(240,240,236)); s.paste(im,(10,10),m)
sm=Image.open(d+"logo.png").resize((48,48)); m2=Image.new("L",(48,48),0); ImageDraw.Draw(m2).ellipse((0,0,47,47),fill=255); s.paste(sm,(340,130),m2)
s.save(d+"logo-preview.png")
