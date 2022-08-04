from django_apscheduler.models import DjangoJob
from rest_framework.serializers import ModelSerializer


class DjangoJobSerializer(ModelSerializer):
    class Meta:
        model = DjangoJob
        fields = ['id', 'next_run_time', 'job_state', 'url']
