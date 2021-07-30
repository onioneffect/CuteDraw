from PIL import Image
import json
from random import choice

def buildTemplate(overrideID : str, template : str):
    try:
        loop = template["template"]
    except KeyError:
        loop = template["sub"]
        _buildSubTemplate(overrideID, loop)
        return

    with open("config.json") as f:
        templateSettings = json.load(f)["templates"][loop]

    templateIMG = Image.open("Templates/{}.png".format(loop))
    coverIMG = Image.open("covers/{}.jpg".format(overrideID))

    box = tuple(templateSettings["coordinates"])
    coverIMG = coverIMG.resize(templateSettings["dimensions"])

    templateIMG.paste(coverIMG, box)
    templateIMG.save("current.jpg")
    return

