
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User

from train_traffic_app.models import TrainTrafficRequest
from train_traffic_app.serializers import TrainTrafficRequestSerializer
from train_traffic_app.serializers import UserSerializer
from train_traffic_app.permissions import IsOwnerOrReadOnly


class TrainTrafficRequestList(generics.ListCreateAPIView):
    """
    List all code train traffic requests, or create a new one.
    """
    queryset = TrainTrafficRequest.objects.all()
    serializer_class = TrainTrafficRequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)

class TrainTrafficRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a train_traffic_request.
    """
    queryset = TrainTrafficRequest.objects.all()
    serializer_class = TrainTrafficRequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer