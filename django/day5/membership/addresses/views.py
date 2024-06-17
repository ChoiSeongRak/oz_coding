from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Address
from .serializers import AddressSerializer
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated 

class AddressList(APIView):
    authentication_classes = [TokenAuthentication] # 고유한 토큰 발급
    permission_classes = [IsAuthenticated] # 인증 확인
    
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

class AddressDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return None
    def get(self, request, pk):
        address = self.get_object(pk)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AddressSerializer(address)
        return Response(serializer.data)
        
class CreateUserAddress(APIView):
    def post(self, request, user_id):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_ERROR)

class UpdateAddress(APIView):
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return None

    def put(self, request, pk):
        address = self.get_object(pk)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteAddress(APIView):
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return None
    def delete(self, request, pk):
        address = self.get_object(pk)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)