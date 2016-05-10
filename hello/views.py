from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from dup_eval import predict


# Create your views here.
def index(request):
    return render(request, 'index.html')

def predict_class(raw_img):
	# img = request.POST["img"]
	pred = predict(raw_img)
	pred_delim = pred.split(',')[1:]
	probs = []
	i = 0
	for p in pred_delim:
		probs.append((p, i))
		i += 1

	probs = sorted(probs, reverse=True)
	toRet = {'results':probs}
	return JsonResponse(toRet)

# def db(request):
#     greeting = Greeting()
#     greeting.save()
#     greetings = Greeting.objects.all()
#     return render(request, 'db.html', {'greetings': greetings})

