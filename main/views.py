from django.shortcuts import render
from .models import Item 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def todo(request):
	todolist = Item.objects.all()
	context = {}
	context["items"] = todolist 


	print "*****"
	if request.method == "POST":
		print "444444"
		task = request.POST.get("task", None)
		findate = request.POST.get("findate", None)
		new_item, created = Item.objects.get_or_create(itemtodo=task)
		new_item.findate = findate
		new_item.save()


	return render(request, "todo.html", context)
