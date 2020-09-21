from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .serializers import NovelSerializer
from .models import Novel


class NovelViewSet(ModelViewSet):
    """ Novel viewset """ 
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny]
        elif self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    
    @action(detail=False)
    def search(self, request):
        title = request.GET.get('title', None)
        filter_kwargs = {}
        if title is not None:
            filter_kwargs['title'] = title
        paginator = self.paginator
        try:
            novels = Novel.objects.filter(**filter_kwargs)
        except ValueError:
            novels = Novel.objects.all()
        results = paginator.paginate_queryset(novels, request)
        serializer = NovelSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)      


