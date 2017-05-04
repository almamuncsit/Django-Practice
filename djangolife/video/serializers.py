from rest_frmaework import ModelSerializers
from .models import Video

class VideoSerializer(ModelSerializers):
    class Meta:
        model = Video