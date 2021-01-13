from rest_framework import serializers
from .models import *


class TblistInquireSerializer(serializers.ModelSerializer):
    child = serializers.SerializerMethodField()
    type = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = TblistInquire
        fields = '__all__'

    def get_type(self, obj):
        return obj.get_type_display()

    def get_child(self, obj):
        if obj.parent is not None:
            return None
        else:
            queryset = TblistInquire.objects.all()
            queryset = queryset.filter(parent=obj.id)
            return TblistInquireSerializer(queryset, many=True).data


class TblistInquireInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblistInquire
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.is_send_email = validated_data['is_send_email']
        instance.send_email_date = validated_data['send_email_date']
        instance.save()
        return instance


class TblistInquireUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblistInquire
        fields = ['is_send_email', 'update_date', 'update_user', 'send_email_date']

    def partial_update(self, instance):
        instance.save()

        return instance


class TblistInquirePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblistInquire
        fields = ['content', 'update_date', 'update_user', 'send_email_date']

