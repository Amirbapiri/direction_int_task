from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult

from core_apps.jobs.tasks import run_spider, fetch_visa_jobs


class JobFetchAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        task = fetch_visa_jobs.delay()
        return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)
