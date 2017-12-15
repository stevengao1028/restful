
from apitest.models import  *
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import  api_view, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth.models import User
# Serializers define the API representation.
class personSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = person
        fields ='__all__'
        # fields = ('created', 'title', 'name', 'age','sex')

# ViewSets define the view behavior.
# class personViewSet(viewsets.ModelViewSet):
#     queryset = person.objects.all()
#     serializer_class = personSerializer

class profitSerializer(serializers.ModelSerializer):
    class Meta:
        model = profit
        # fields = '__all__'
        fields = ('year', 'quarter', 'stk_code', 'stk_name','roe')

# ViewSets define the view behavior.
# class profitViewSet(viewsets.ModelViewSet):
#     queryset = profit.objects.all()
#     serializer_class = profitSerializer



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'person', personViewSet)
# router.register(r'profit', profitViewSet)