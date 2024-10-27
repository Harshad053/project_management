from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project, UserProject

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()  

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'updated_at', 'created_by']


class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.client_name', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client_name', 'created_at', 'created_by']


class ProjectCreateSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']
        read_only_fields = ['created_by']  


    def create(self, validated_data):
        users = validated_data.pop('users', [])
        validated_data['created_by'] = self.context['request'].user  
        project = Project.objects.create(**validated_data)
        project.users.set(users)
        return project
