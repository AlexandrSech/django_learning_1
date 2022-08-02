from rest_framework import viewsets, views, response
from .models import MyUser
from .serializers import MyUserSimpleSerializer, MyUserSerializer


class MyUsersListView(views.APIView):
    def get(self, request, format=None):
        users = MyUser.objects.all()
        serializer = MyUserSimpleSerializer(users, many=True)
        return response.Response(serializer.data)


class MyUsersViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
