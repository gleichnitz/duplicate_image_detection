from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from dup_eval import predict
from django.views.decorators.csrf import csrf_exempt
import base64
from PIL import Image

import numpy as np
from scipy import misc

# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def predict_class(request):
	img = request.POST["image"]
	starter = img.find(',')
	img = img[(starter+1):]
	raw_img = base64.b64decode(img)
	f = open('myimage.png','w+',0)
	f.write(raw_img)

	im = misc.imread('myimage.png')[:,:,0:3]
	print im.shape

	pred = predict(im).split(',')[1:]
	i = 0
	probs = []
	for p in pred:
		probs.append((float(p)*100,i))
		i += 1

	probs = sorted(probs, reverse=True)
	print probs
	toRet = {'result' : probs}
	return JsonResponse(toRet)

	pred = predict(raw_img)
	# pred_delim = pred.split(',')[1:]
	# probs = []
	# i = 0
	# for p in pred_delim:
	# 	probs.append((p, i))
	# 	i += 1

	# probs = sorted(probs, reverse=True)
	# toRet = {'results':probs}
	# return JsonResponse(toRet)

# def db(request):
#     greeting = Greeting()
#     greeting.save()
#     greetings = Greeting.objects.all()
#     return render(request, 'db.html', {'greetings': greetings})

