from rest_framework import serializers
from skynet.models import Messages


class SkynetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('state', 'city', 'username', 'message')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')