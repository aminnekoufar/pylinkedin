from django.contrib.auth import get_user_model
from rest_framework import serializers

from pylinkedin.users.models import Education as UserEducation
from pylinkedin.users.models import User as UserType

User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    education = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["username", "name", "url", "location", "gender", "avatar", "education"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }


class UserEducationSerializer(serializers.ModelSerializer[UserEducation]):
    user = serializers.CharField(read_only=True)
    lookup_field = "pk"

    class Meta:
        model = UserEducation
        lookup_field = "pk"
        fields = ["institution", "user", "degree", "field_of_study", "start_date", "end_date", "description", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:educations-detail", "lookup_field": "pk"},
        }
