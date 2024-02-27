from rest_framework import serializers

from movies.models import Movie


def title_length_validator(value):
    if len(value) < 10:
        raise serializers.ValidationError("Title is too short")
    if len(value) > 100:
        raise serializers.ValidationError("Title is too long")
    return value


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(validators=[title_length_validator])
    description = serializers.CharField()
    year = serializers.IntegerField()
    active = serializers.BooleanField(default=True)

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

    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and description must be different")
        return data
