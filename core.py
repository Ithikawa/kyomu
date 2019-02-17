# -*- Coding: utf-8 -*-
import argparse
from enum import Enum
import io
import codecs

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw

class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5

def get_document_bounds(image_file):
    """Returns document bounds given an image."""
    client = vision.ImageAnnotatorClient()

    bounds = []

    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    response = client.document_text_detection( image = types.Image(content=content), image_context= {'language_hints': "ja"})
    document = response.full_text_annotation

    temp = str(document).encode().decode("unicode_escape").encode("raw_unicode_escape").decode("utf-8")

    # Collect specified feature bounds by enumerating all document features
    return temp

def render_doc_text(filein, fileout):
    image = Image.open(filein)
    documents = get_document_bounds(filein)

    f = codecs.open( fileout, "w","utf-8")
    f.write( str(documents) )
    f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('detect_file', help='The image for text detection.')
    parser.add_argument('-out_file', help='Optional output file', default=0)
    args = parser.parse_args()

    parser = argparse.ArgumentParser()
    render_doc_text(args.detect_file, args.out_file)