from PIL import Image, ImageDraw, ImageFont

# 画像全体に対するメッセー描写可能エリアの比率
MAX_RATIO = 0.8

FONT_MAX_SIZE = 256
FONT_MIN_SIZE = 24

FONT_NAME = "/Library/Fonts/Arial Bold.ttf"
FONT_COLOR_WHITE = (255, 255, 255, 0)

OUTPUT_NAME = "output.png"
OUTPUT_FORMAT = "PNG"


def save_with_message(fp, message):
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)

    image_width, image_height = image.size  # (800, 300)など出力される
    message_area_width = image_width * MAX_RATIO
    message_area_height = image_height * MAX_RATIO

    for font_size in range(FONT_MAX_SIZE, FONT_MIN_SIZE, -1):
        font = ImageFont.truetype(FONT_NAME, font_size)
        text_width, text_height = draw.textsize(message, font=font)
        # draw.textsize(text, options)で引数で指定されたテキストのサイズ（タプル形式（76, 78）など）を返してくれる
        # つまりx方向76,y方向78のテキストボックスであることがわかる、この情報があれば画像のどこに配置するか計算することができる
        w = message_area_width - text_width
        h = message_area_height - text_height

        # 幅、高さともに領域内におさまる値を採用
        if w > 0 and h > 0:
            position = ((image_width - text_width) / 2,
                        (image_height - text_height) / 2)
            draw.text(position, message, fill=FONT_COLOR_WHITE, font=font)
            break

    image.save(OUTPUT_NAME, OUTPUT_FORMAT)
