import os
import re
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from unidecode import unidecode
from youtubesearchpython.__future__ import VideosSearch
from ZeMusic import app
from config import YOUTUBE_IMG_URL

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

def clear(text):
    list = text.split(" ")
    title = ""
    for i in list:
        if len(title) + len(i) < 60:
            title += " " + i
    return title.strip()

async def get_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"cache/thumb{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(10))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.5)

        # Make the thumbnail circular and increase its size by 10%
        circular_image = youtube.convert("RGBA")
        circular_image = changeImageSize(385, 385, circular_image)  # Resize to 385x385 (10% larger)

        # Create a mask to make the image circular
        mask = Image.new("L", circular_image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + circular_image.size, fill=255)

        # Apply the mask to the circular image
        circular_image.putalpha(mask)

        # Calculate the center position for the circular image
        center_x = (1280 - circular_image.size[0]) // 2
        center_y = (720 - circular_image.size[1]) // 2 - 100  # Adjust Y position as needed

        # Paste the circular image onto the background
        background.paste(circular_image, (center_x, center_y), circular_image)

        draw = ImageDraw.Draw(background)
        font_large = ImageFont.truetype("ZeMusic/assets/font.ttf", 50)
        font_medium = ImageFont.truetype("ZeMusic/assets/font2.ttf", 35)
        font_small = ImageFont.truetype("ZeMusic/assets/font2.ttf", 30)

        # Calculate the center positions for the text
        text_start_y = center_y + circular_image.size[1] + 20
        draw.text((center_x, text_start_y), "AFROTOO MUSIC", fill="white", font=font_large, anchor="ms")
        draw.text((center_x, text_start_y + 60), "Aghs Lab Safety Rap", fill="white", font=font_medium, anchor="ms")
        draw.text((center_x, text_start_y + 110), f"Views: {views}", fill="white", font=font_small, anchor="ms")
        draw.text((center_x, text_start_y + 160), f"Duration: {duration}", fill="white", font=font_small, anchor="ms")
        draw.text((center_x, text_start_y + 210), f"Channel: {channel}", fill="white", font=font_small, anchor="ms")

        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        background.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL
