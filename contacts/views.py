from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from .tasks import send_admin_message
from celery.result import AsyncResult
from .forms import ContactForm


# Create your views here.
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        # send_admin_message()  # simple call
        if form.is_valid():
            message = form.cleaned_data["message"]
            task_result = send_admin_message.delay(message=message)
            print(type(task_result))
            print(task_result)

            print(task_result.ready())
            print(task_result.state)

            return HttpResponseRedirect("/contacts/")

    form = ContactForm()
    return render(request, "contacts/contacts.html", {"form": form})


# Для проверки статуса в live режиме


def status_view(request, task_id):
    task_result = AsyncResult(task_id)

    result = None
    if task_result.ready():
        result = task_result.get()

    context = {"task_result": task_result, "result": result}
    return render(request, "contacts/status.html", context)


def about_view(request):
    return render(request, "contacts/about.html")
