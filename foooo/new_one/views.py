from django.shortcuts import render, HttpResponse, redirect
from .models import MyUser
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateUserForm
import json

from .internal_logic.custom_parcer import parcer

from .serializers import MyUserSimpleSerializer
from rest_framework.renderers import JSONRenderer

import logging

logger = logging.getLogger(__name__)



def hello(request):
    # users = MyUser.objects.all()
    # emails = []
    # for user in users:
    #     emails.append(user.email)
    # return HttpResponse("Hello world!" + str(emails))

    logger.info("info hello")
    logger.debug("debug hello")
    logger.warning("warning hello")
    logger.error("error hello")

    serialized_data = MyUserSimpleSerializer(MyUser.objects.get(pk=1))
    return HttpResponse(JSONRenderer().render(serialized_data.data))


def new(request):
    print(request.user)

    print(request.GET)

    print(parcer())

    result = {"users": []}
    for line in MyUser.objects.all():
        result["users"].append({
            "id": line.id,
            "first_name": line.first_name,
            "last_name": line.last_name,
            "email": line.email,
        })
    return HttpResponse(json.dumps(result))


@csrf_exempt
def create_user(request):
    args = {"method": request.method.lower()}
    if request.method == "POST":
        try:
            new_user = CreateUserForm(request.POST).save()
            args.update({"user_name": f"{new_user.first_name} {new_user.last_name}"})
        except Exception as create_ex:
            logger.error(str({"error_message": create_ex}))
            args.update({"error_message": create_ex})

    return render(request, "new_one/create_user.html", args)


from django.views import View
from django.views import View, generic


class CreateUserView(generic.ListView):
    def get(self, request):
        return render(request, "new_one/create_user.html")
    def post(self, request):
        CreateUserForm(request.POST).save()
        return HttpResponse(f"post")


class UsersListView(generic.ListView):

    def get(self, request):
        return render(request, "new_one/users_list.html", {"users": MyUser.objects.all()})


def user(request):
    res = MyUser.objects.get(id=3)
    return render(request, "new_one/user.html", {"user_name": f"{res.first_name} {res.last_name}"})
