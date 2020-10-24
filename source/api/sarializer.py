# from rest_framework import serializers
# from webapp.models import Photo
#
#
# class PhotoSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     picture = serializers.ImageField(upload_to='uploads', required=True)
#     text = serializers.CharField(max_length=3000, required=True)
#     author = serializers.PrimaryKeyRelatedField(read_only=True)
#     created_date = serializers.DateTimeField(read_only=True)
#     favorites = serializers.ManyRelatedField(read_only=True)
#
#     def create(self, validated_data):
#         return Photo.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         return instance
