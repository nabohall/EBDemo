from django.shortcuts import render

# Create your views here.
from .models import Element
from django.http import HttpResponseRedirect
from django.urls import reverse

#Print every element in the database
def index(request):
	sequenceList = Element.objects.all()
	out = [str(e) for e in sequenceList]
	context = {
		'out': out,
		'server' : get_client_ip(request),
	}
	return render(request, 'fibseq/index.html', context)

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip
#shows the list of elements up to that point
def sequence(request, p):
	pos = int(p)
	seq = Element.objects.all()[:pos]
	out = [str(e) for e in seq]
	return render(request, 'fibseq/sequence.html',{'out': out})

"""
Generate the fibonacci sequence up to Pos.
"""
def generate(request):
	try:
		pos = int(request.POST['generate'])
		#Try to get element at that position. Getting all the elements,
		#will be handled in finally
		Element.objects.get(position=pos)
	except (ValueError, KeyError):
		#Go back to index
		return render(request, 'fibseq/index.html', {'error_message': "Please enter a number."})
	except (Element.DoesNotExist, IndexError):
		#generate elements until point
		pos = int(request.POST['generate'])
		last, secondToLast = Element.objects.all().order_by('-position')[:2]
		a, b = secondToLast.value, last.value
		for i in range(last.position, pos):
			a, b = b, a+b
			ele = Element(value=b, position=(i+1))
			ele.save()
	finally:
		#redirect to sequence, which will display the sequence
		p = chr(int(request.POST['generate']))
		return HttpResponseRedirect(reverse('sequence',args=(pos,)))