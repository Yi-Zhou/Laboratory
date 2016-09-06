from django.http import JsonResponse

def deco(func):
	def wrapper(request, *args, **kwargs):
		print 'in wrapper'
		print 'request: %s'%request
		print args
		print kwargs
		return func(request, *args, **kwargs)
	return wrapper	

def MethodRequired(method, msg = 'Method <%s> is required', status = 405, safe = False):
	return JsonResponse(dict(ok = False, msg = msg%method), status = status, safe = safe)

def method_required(required_method):
	def _decorator(func):
		def _wrapper(request, *args, **kwargs):
			if request.method != required_method:
				return MethodRequired(required_method)
			else:
				return func(request, *args, **kwargs)
		return _wrapper
	return _decorator

class Request():
	
	def __init__(self, method):
		self.method = method

@method_required('POST')
def view(request):
	print request
	return JsonResponse({'ok': True})

request = Request('POST')

print view(request)
request.method = 'GET'
print view(request)

