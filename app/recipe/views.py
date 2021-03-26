from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Tag
from recipe import serializers

class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')

    """Validated Serializer"""
    def perform_create(self, serializer):
        """Create a new ingredient"""
        print("Request Data")
        print(self.request.data)
        print(self.request.user)
        serializer.save(user=self.request.user)
