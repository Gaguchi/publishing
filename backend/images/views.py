from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer

class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        section = request.data.get('section')
        if not section:
            return Response({'error': 'Section is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Delete existing image in the section if it exists
        Image.objects.filter(section=section).delete()
        
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image_instance = serializer.save()
            image_url = request.build_absolute_uri(image_instance.image.url)
            return Response({'image': image_url}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageListView(APIView):
    def get(self, request, *args, **kwargs):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)