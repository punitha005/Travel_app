from rest_framework import generics, status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from .models import Destination
from .serializers import DestinationSerializer

class DestinationListCreate(generics.ListCreateAPIView):
    """
    A view to list and create destination objects.
    """
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def handle_exception(self, exc):
        """
        Handle exceptions globally and return appropriate responses.
        """
        if isinstance(exc, NotFound):
            return Response({"detail": "Resource not found."}, status=status.HTTP_404_NOT_FOUND)
        elif isinstance(exc, PermissionDenied):
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        return super().handle_exception(exc)

class DestinationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    A view to retrieve, update, and delete a destination object.
    """
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def handle_exception(self, exc):
        """
        Handle exceptions globally and return appropriate responses.
        """
        if isinstance(exc, NotFound):
            return Response({"detail": "Resource not found."}, status=status.HTTP_404_NOT_FOUND)
        elif isinstance(exc, PermissionDenied):
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        return super().handle_exception(exc)
