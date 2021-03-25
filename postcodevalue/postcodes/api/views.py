from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from postcodes.api.models import Outcode, NexusOutcode
from postcodes.api.serializers import OutcodeSerializer, NexusSerializer


class OutcodeListCreateAPIView(APIView):

    def get(self, request):
        outcodes = Outcode.objects.filter()
        serializer = OutcodeSerializer(outcodes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OutcodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OutcodeDetailsAPIView(APIView):

    def get_object(self, outcode_code):
        outcode = get_object_or_404(Outcode, outcode_code=outcode_code)
        return outcode
    
    def get(self, request, outcode_code):
        outcode = self.get_object(outcode_code)
        serializer = OutcodeSerializer(outcode)
        return Response(serializer.data)

    def put(self, request, outcode_code):
        outcode = self.get_object(outcode_code)
        serializer = OutcodeSerializer(outcode, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, outcode_code):
        outcode = self.get_object(outcode_code)
        outcode.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-------------------------------------------------------------

class NexusListCreateAPIView(APIView):

    def get(self, request):
        outcodes = NexusOutcode.objects.filter()
        serializer = NexusSerializer(outcodes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NexusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class NexusDetailsAPIView(APIView):

#     def get_object(self, outcode_code):
#         outcode = get_object_or_404(NexusOutcode, outcode_code=outcode_code)
#         return outcode
    
#     def get(self, request, outcode_code):
#         outcode = self.get_object(outcode_code)
#         serializer = NexusSerializer(outcode)
#         return Response(serializer.data)

class NexusDetailsAPIView(generics.RetrieveAPIView):
    serializer_class = NexusSerializer
    queryset = NexusOutcode.objects.all()

    def get_object(self, outcode_code):
        outcode = get_object_or_404(NexusOutcode, outcode_code=outcode_code)
        return outcode

    def get(self, request, outcode_code):
        outcode = self.get_object(outcode_code)
        serializer = NexusSerializer(outcode)
        return Response(serializer.data)

    # def put(self, request, outcode_code):
    #     outcode = self.get_object(outcode_code)
    #     serializer = NexusSerializer(outcode, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, outcode_code):
    #     outcode = self.get_object(outcode_code)
    #     outcode.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


