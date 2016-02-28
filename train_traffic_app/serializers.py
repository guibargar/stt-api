from rest_framework import serializers
from train_traffic_app.models import TrainTrafficRequest
from django.contrib.auth.models import User


class TrainTrafficRequestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = TrainTrafficRequest
        fields = ('id','owner','station','requestType')

class UserSerializer(serializers.ModelSerializer):
    trainTrafficRequests = serializers.PrimaryKeyRelatedField(many=True, queryset=TrainTrafficRequest.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'trainTrafficRequests')