from rest_framework import generics
from django.shortcuts import get_object_or_404, redirect
from .models import Projects
from .serializers import PortfolioProjectSerializer

class ProjectListAPI(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = PortfolioProjectSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        project_id = self.request.query_params.get('id')  # get ?id= value
        if project_id is not None:
            queryset = queryset.filter(id=project_id)
        return queryset
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

def project_redirect_view(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    return redirect(project.live_url)
