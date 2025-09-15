from rest_framework import serializers
from .models import Projects

class PortfolioProjectSerializer(serializers.ModelSerializer):
    redirect_url = serializers.SerializerMethodField()

    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'image', 'redirect_url', 'date_added']

    def get_redirect_url(self, obj):
        # This gives the frontend a backend route, not the live URL directly
        request = self.context.get('request')
        return request.build_absolute_uri(f"/api/projects/{obj.id}/redirect/")
