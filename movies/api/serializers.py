from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    year = serializers.IntegerField()
    active = serializers.BooleanField(default=True)
    
    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Title is too short")
        if len(value) > 100:
            raise serializers.ValidationError("Title is too long")
        return value

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.year = validated_data.get("year", instance.year)
        instance.active = validated_data.get("active", instance.active)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()
        return instance