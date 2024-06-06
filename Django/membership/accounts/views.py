from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from addresses.serializers import AddressSerializer
from .models import User
from rest_framework.exceptions import NotFound
from addresses.models import Address


    
class UserAddress(APIView):
    def get_object(self, user_id):
        try:
            return Address.objects.get(id=user_id)
        except Address.DoesNotExist:
            raise NotFound
        
    def get(self, request, user_id):
        address = self.get_object(user_id)
        
        
        serializer = AddressSerializer(address)
        
        return Response(serializer.data)  
        
    def post(self, request, user_id):
        address = self.get_object(user_id)
        
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            address = serializer.save(user=request.user)
            
            serializer = AddressSerializer(address)
            
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)