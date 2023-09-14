from.models import *
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveAPIView , DestroyAPIView ,ListCreateAPIView ,RetrieveUpdateAPIView , RetrieveDestroyAPIView

from .serializers import StudentSerializer

# Create your views here.


class studentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
class studentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class studentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class studentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class studentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
class studentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class studentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer