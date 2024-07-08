from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from . import functions
import matplotlib
import matplotlib.pyplot as plt
import os
import cv2
matplotlib.use('Agg')

# Create your views here.



def create(request):
    fake_images = functions.get_image()
    images_dir = os.path.join(settings.BASE_DIR, 'static/images')
    img_urls = []
    for no, image in enumerate(fake_images):
        image_path = os.path.join(images_dir, f'fake_image{no}.png')
        img_urls.append(f'images/fake_image{no}.png')
        plt.axis('off')
        plt.imshow(image)
        plt.savefig(image_path)
    context = {'img_urls': img_urls}
    return render(request, "display/images.html", context)