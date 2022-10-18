from PIL import Image, ImageDraw, ImageFont


def save_compressed(img):
    img.save("./imgs/test1.jpg", "JPEG",  optimize=True, qualitiy = 1)



def watermark(img):
    watermarked = ImageDraw(img)
    watermarked.text((5, 2), "Can")
    watermarked.bitmap((12, 9), Image.open("./imgs/test.png").resize((50, 50)))

if __name__ == "__main__":
    img = Image.open("./imgs/test.jpg")
    save_compressed(img)
    img.show()