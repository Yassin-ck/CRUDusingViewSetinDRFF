from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response


class StudentViewset(viewsets.ViewSet):
    
    def list(self,request):
        print('============list===========')
        print('basename:',self.basename)
        print('action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        print('description:',self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu , many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        print('============retrieve===========')
        print('basename:',self.basename)
        print('action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        print('description:',self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
    
    
    def create(self,request):
        print('============create===========')
        print('basename:',self.basename)
        print('action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        print('description:',self.description)
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created...'},status=status.HTTP_201_CREATED)
        return(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
    
    def update(self,request,pk=None):
        print('============update===========')
        print('basename:',self.basename)
        print('action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        print('description:',self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated...'})
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def partial_update(self,request,pk=None):
        print('============partial_update===========')
        print('basename:',self.basename)
        print('action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        print('description:',self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu,data=request.data,partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Partial Data Updated...'})
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        
    def destroy(self,request,pk=None):
        print('============delete===========')
        print('basename:',self.basename)
        print('action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        print('description:',self.description)
        id = pk 
        if id is not None:
            stu = Student.objects.get(pk=id)
            stu.delete()
            return Response({'msg':'Data Deleted !!!'})
            