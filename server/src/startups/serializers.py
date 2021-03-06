from rest_framework.serializers import ModelSerializer
from core.models import Student


class StudentSerializer(ModelSerializer):
    """serializer for student object"""

    class Meta:
        model = Student
        fields = [
            "StudentId",
            "FirstName",
            "LastName",
            "ComChannel",
            "Groups",
            "Gender",
        ]
