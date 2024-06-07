from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AddressSerializer
from .models import Address
from rest_framework.exceptions import NotFound

from addresses import serializers
from rest_framework.authentication import TokenAuthentication # 사용자 인증
from rest_framework.permissions import IsAuthenticated # 권한 부여


class AddressList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        
        return Response(serializer.data)
    
class AddressDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, address_id):
        try:
            return Address.objects.get(id=address_id)
        except Address.DoesNotExist:
            raise NotFound
        
    def put(self, request, address_id):
        address = self.get_object(address_id)
        
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            address = serializer.save(user=request.user)
            
            serializer = AddressSerializer(address)
            
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)
        
class AddressDelete(APIView):
    def get_object(self, address_id):
        try:
            return Address.objects.get(id=address_id)
        except Address.DoesNotExist:
            raise NotFound
    
    def delete(self, request, address_id):
        address = self.get_object(address_id)
        address.delete()
        
        

