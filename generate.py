from typing import List
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageSequence
import random


class GifGenerator:
    def __init__(self, image_path: str, num_frames: int, text: str) -> None:
        self.__image_path = image_path
        self.__num_frames = num_frames
        self.__text = text

    def generate(self) -> None:
        base_image = Image.open(self.__image_path)

        # Create a list to hold the frames of the gif
        frames = list()

        # Generate multiple frames with random rainbow filters
        for _ in range(self.__num_frames):
            filtered_image = self.__random_rainbow_filter(base_image.copy())
            frames.append(self.__add_text_to_bottom(filtered_image, self.__text))

        # Save as GIF
        frames[0].save(
            "output.gif",
            save_all=True,
            append_images=frames[1:],
            optimize=False,
            duration=100,
            loop=0,
        )

    @staticmethod
    def __random_rainbow_filter(image: Image):
        # Generate random RGB values
        red: int = random.randint(0, 255)
        green: int = random.randint(0, 255)
        blue: int = random.randint(0, 255)

        # Apply the filter using Image.point()
        lookup_table: List[List[int]] = list()
        for i in range(256):
            lookup_table.extend([(i + red) % 256, (i + green) % 256, (i + blue) % 256])
        return image.point(lookup_table)

    @staticmethod
    def __add_text_to_bottom(image, text: str):
        # Get image width and height
        width, height = image.size

        # Load a font
        font = ImageFont.truetype("arial.ttf", 40)

        # Create a drawing context
        draw = ImageDraw.Draw(image)

        # Calculate text width and height
        # text_width, text_height = draw.textsize(text, font=font)  # This line was the issue
        # font = ImageFont.truetype("sans-serif.ttf", 16)
        # draw.text((x, y),"Sample Text",(r,g,b))
        # draw.text((0, 0),"Sample Text",(255,255,255),font=font)
        # Calculate X, Y position of the text
        # x = (width - text_width) // 2
        # y = height - text_height - 10  # 10 pixels from the bottom
        x, y = 0, 150
        # Draw the text onto the image
        draw.text((x, y), text, font=font, fill=(255, 255, 255))

        return image


def main() -> None:
    GifGenerator(image_path="image.jpg", num_frames=10, text="Text!").generate()


if __name__ == "__main__":
    main()
