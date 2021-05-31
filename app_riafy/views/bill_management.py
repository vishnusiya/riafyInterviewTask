import requests, os
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
# import tesseract

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import re

##function for getting Bill Details
@require_POST
def bill_details_get(request):
    try:
        data_dict = {}
        if 'bill_image' in request.FILES:
            file = request.FILES['bill_image']
            path = default_storage.save('bill.png', ContentFile(file.read())) 
            file_path = 'media/' + 'bill.png'
            response = pytesseract.image_to_string(file_path)
            if 'consumer#' in response: 
                net_payable_amount = re.search(r'Last Paid Amount - Rs.(.*?)a', response).group(1)
                consumer_number = re.search(r'consumer#(.*?)sit', response).group(1)
                bill_number = re.search(r'Bill#(.*?)Bill', response).group(1)
                data_dict['consumer_number'] = consumer_number
                data_dict['bill_number'] = bill_number
                data_dict['net_payable_amount'] = net_payable_amount
                os.remove(file_path)
                return HttpResponse(content=json.dumps(data_dict), status=200, content_type="application/json")
            else:
                os.remove(file_path)
                return HttpResponse(content=json.dumps("Please Upload Valid Bill"), status=406, content_type="application/json")
        else:
            return HttpResponse(content=json.dumps("Please Upload Bill"), status=406, content_type="application/json")
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = "\n".join(traceback.format_exception(*sys.exc_info()))
        print(err)
        return HttpResponse(content=json.dumps(err), status=406, content_type="application/json")

