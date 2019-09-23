""" Company views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from src.api.serializers.company import CompanySerializer
from src.api.models import Company

class CompanyListCreateAPIView(ListCreateAPIView):
    """ List/Create companies"""
    permission_classes =(IsAuthenticated,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
