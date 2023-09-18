from board.models import Board, Task
from rest_framework import serializers
from team.models import Team


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class BoardPostSerializer(serializers.ModelSerializer):
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    class Meta:
        model = Board
        fields = ['name', 'description', 'team_id']

class BoardGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name']




class TaskSerializer(serializers.ModelSerializer):
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    class Meta:
        model = Task
        fields = ["board_id", "title", "description", 'team_id', 'status', 'creation_time']
    


class TaskPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'status']