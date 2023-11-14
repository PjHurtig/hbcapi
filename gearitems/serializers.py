from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import GearItem


class GearItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the GearItem model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = GearItem
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'gearlist', 'created_at', 'updated_at', 'name', 'about', 'image',
        ]


class GearItemDetailSerializer(GearItemSerializer):
    """
    Serializer for the GearItem model used in Detail view
    """
    gearlist = serializers.ReadOnlyField(source='gearlist.id')
