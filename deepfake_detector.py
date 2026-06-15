
from transformers import pipeline
from PIL import Image

detector = pipeline(
    "image-classification",
    model="umm-maybe/AI-image-detector"
)

def detect_fake_image(image_path):

    image = Image.open(image_path)

    result = detector(image)

    return result
