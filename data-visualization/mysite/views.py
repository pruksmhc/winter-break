from stock import getDataToFrontEnd
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def getIndustryStock(request):
	print("IN INDUSTRY STOCK")
	jsonStr= getDataToFrontEnd() 
	#jsonStr = json.dumps(jsonStr)
	jsonStr = json.dumps(jsonStr)
	print("know sending back")
	print(type(jsonStr))
	return HttpResponse(jsonStr, content_type='json')