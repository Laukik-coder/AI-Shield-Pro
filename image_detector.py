
from transformers import pipeline
from PIL import Image

classifier = pipeline(
    "image-classification",
    model="microsoft/resnet-50"
)

def detect_image(image_path):

    image = Image.open(image_path)

    result = classifier(image)

    return result
