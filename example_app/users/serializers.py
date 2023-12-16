from collections import OrderedDict

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import User


class AuthUserSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'password_2',
        ]

        extra_kwargs = {
            'password': {
                'required': False,
                'write_only': True,
            },
        }

    def get_fields(self) -> OrderedDict:
        fields = super().get_fields()
        request = self.context.get('request')

        if getattr(request, 'method', str()).upper() in ['PUT', 'PATCH']:
            fields['username'].read_only = True
        else:
            fields['password'].required = True

        return fields

    def validate(self, attrs: dict) -> dict:
        password = attrs.get('password')
        password_2 = attrs.get('password_2')

        if password is not None:
            if password_2 is None:
                raise serializers.ValidationError({'password_2': [_("You must confirm your password.")]})

            if password != password_2:
                raise serializers.ValidationError({'password': [_("Your passwords do not match.")]})

            try:
                validate_password(password)
            except DjangoValidationError as e:
                raise serializers.ValidationError({'password': e.messages})

            attrs.pop('password_2')

        return attrs


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_2 = serializers.CharField(required=False)

    class Meta:
        model = User

        fields = [
            'old_password',
            'new_password',
            'new_password_2'
        ]

    def validate(self, attrs: dict) -> dict:
        new_password = attrs.get('new_password')
        new_password_2 = attrs.get('new_password_2')

        if new_password is not None:
            if new_password_2 is None:
                raise serializers.ValidationError({'new_password_2': [_("You must confirm your new password.")]})

            if new_password != new_password_2:
                raise serializers.ValidationError({'new_password': [_("Your new passwords do not match.")]})

            try:
                validate_password(new_password)
            except DjangoValidationError as e:
                raise serializers.ValidationError({'new_password': e.messages})

            attrs.pop('new_password_2')

        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
