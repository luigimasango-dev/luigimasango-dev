import asyncio
from playwright.async_api import async_playwright
from PIL import Image, ImageDraw
d="C:/Dev/gh-profile/logo/"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":512,"height":512})
        for n in ("crate","route","monogram"):
            await pg.goto("file:///"+d+f"logo-{n}.svg"); await pg.screenshot(path=d+f"logo-{n}.png")
        await b.close()
asyncio.run(main())
sheet=Image.new("RGB",(3*300+40,340),(240,240,236))
for i,n in enumerate(("crate","route","monogram")):
    im=Image.open(d+f"logo-{n}.png").resize((260,260))
    m=Image.new("L",(260,260),0); ImageDraw.Draw(m).ellipse((0,0,259,259),fill=255)
    sheet.paste(im,(20+i*300,20),m)
    sm=Image.open(d+f"logo-{n}.png").resize((40,40)); m2=Image.new("L",(40,40),0); ImageDraw.Draw(m2).ellipse((0,0,39,39),fill=255)
    sheet.paste(sm,(130+i*300,288),m2)
sheet.save(d+"logo-options.png")
