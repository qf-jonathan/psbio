from django.contrib.auth.models import User, Group, Permission
from core.models import Dispositivo, Persona, Horario, Registro
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'groups', 'user_permissions', 'is_superuser')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'id', 'name', 'permissions')


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ('url', 'id', 'name')


class DispositivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ('url', 'id', 'codigo', 'nombre', 'descripcion')


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    dispositivo = serializers.PrimaryKeyRelatedField(queryset=Dispositivo.objects.all())
    dispositivo_name = serializers.StringRelatedField(source='dispositivo', read_only=True)

    class Meta:
        model = Persona
        fields = ('url', 'id', 'codigo', 'paterno', 'materno', 'nombres', 'email', 'dispositivo', 'dispositivo_name')


class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horario
        fields = ('url', 'id', 'nombres', 'descripcion', 'inicio', 'final')


class RegistroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registro
        fields = ('url', 'id', 'marca', 'persona')
