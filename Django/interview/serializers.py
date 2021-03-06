from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Sprint, Task
from rest_framework.reverse import reverse

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active',)

    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': reverse('user-detail', kwargs={User.USERNAME_FIELD: username}, request=request),
        }


class SprintSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField(source='get_links')

    class Meta:
        model = Sprint
        fields = ('id', 'name', 'description', 'end')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('sprint-detail', kwargs={'pk': obj.pk}, request=request),
        }


class TaskSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fileds = ('id', 'name', 'description', 'sprint', 'status', 'status_display', 'order',
                  'started', 'due', 'completed',)

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('task-detail', kwargs={'pk': obj.pk}, request=request),
        }
