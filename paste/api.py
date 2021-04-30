from paste.models import Paste
from rest_framework import serializers, viewsets, routers

class PasteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paste
        fields = "__all__"

class PasteViewSet(viewsets.ModelViewSet):
    serializer_class = PasteSerializer
    queryset = Paste.objects.all()


router = routers.DefaultRouter()
router.register("paste", PasteViewSet)