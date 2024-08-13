from rest_framework import viewsets
from .models import ImageUpload, Template
from .serializers import ImageUploadSerializer, TemplateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from reportlab.pdfgen import canvas
from django.http import FileResponse
import io

class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

@api_view(['POST'])
def generate_pdf(request):
    images = request.data.get('images')
    template_id = request.data.get('template_id')
    # Generate PDF logic here using ReportLab
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    # Add images to PDF
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='output.pdf')