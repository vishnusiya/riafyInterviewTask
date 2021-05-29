import requests
import json, base64, traceback, sys
from django.core.files import File
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
from pytesseract import image_to_string
import pytesseract

from pytesseract import *
from PIL import Image


##function for getting Bill Details
@require_POST
def bill_details_get(request):
    try:
        if 'bill_image' in request.FILES:
            bill_image = request.FILES['bill_image']
            print('bill_image',bill_image)
            # print(1111111111,pytesseract.image_to_string(Image.open('/home/vishnupriya/riafy.jpg')))
            # pytesseract.tesseract_cmd = '/home/vishnupriya//projects/shopApp/venv/lib/python3.8/site-packages/tesseract'
            # print(111111122222222111,pytesseract.image_to_string(Image.open(bill_image)))
            # # print(pytesseract.image_to_string('/home/riafy.jpg'))
        

        # Sample Data
        data_dict = {}
        data_dict['consumer_number'] = 2278
        data_dict['bill_number'] = 13678
        data_dict['net_payable_amount'] = 1700
        return HttpResponse(content=json.dumps(data_dict), status=200, content_type="application/json")
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = "\n".join(traceback.format_exception(*sys.exc_info()))
        print(err)
        return HttpResponse(content=json.dumps(err), status=406, content_type="application/json")

