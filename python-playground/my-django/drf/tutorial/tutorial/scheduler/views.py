import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.core.management.base import BaseCommand
from django_apscheduler import util
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJob, DjangoJobExecution
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from tutorial.scheduler.serializers import DjangoJobSerializer

logger = logging.getLogger(__name__)


def my_job():
    # Your job processing logic here...
    print('success')


class DjangoJobViewSet(viewsets.ModelViewSet):
    serializer_class = DjangoJobSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = DjangoJob.objects.all()
    serializer = DjangoJobSerializer

    def create(self, request, *args, **kwargs):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
        return super().create(request, *args, **kwargs)

    def destroy(self, request, pk=None):
        print(request)
        return Response('success')
