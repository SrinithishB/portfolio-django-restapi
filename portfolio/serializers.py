from rest_framework import serializers
from .models import *

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields=['id','pname','pdescription','link']