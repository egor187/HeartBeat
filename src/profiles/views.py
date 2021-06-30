from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.http import Http404

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from .models import CustomUser
from .serializers import ProfileSerializer


class ProfileListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer



# class ProfileListView(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = CustomUser.objects.all()
#     serializer_class = ProfileSerializer
#
#     def get(self, requset, *args, **kwargs):
#         return self.list(requset, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class ProfileDetailView(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = CustomUser.objects.all()
#     serializer_class = ProfileSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         self.destroy(request, *args, **kwargs)



# class ProfileListView(APIView):
#     def get(self, request):
#         profile_list = CustomUser.objects.all()
#         serializer = ProfileSerializer(profile_list, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ProfileSerializer(request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# class ProfileDetailView(APIView):
#     @staticmethod
#     def get_object(pk):
#         try:
#             profile = CustomUser.objects.get(pk=pk)
#             return profile
#         except CustomUser.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)
#
#     def put(self, requset, pk):
#         profile = self.get_object(pk)
#         data = request.data
#         serializer = ProfileSerializer(instance=profile, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         profile = self.get_object(pk)
#         profile.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# @csrf_exempt
# @api_view(["GET", "POST"])
# def profile_list_view(request):
#     if request.method == "GET":
#         profile_list = CustomUser.objects.all()
#         serializer = ProfileSerializer(profile_list, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ProfileSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=404)


# # @csrf_exempt
# @api_view(["GET", "POST", "PUT", "DELETE"])
# def profile_detail_view(request, pk):
#     try:
#         instance = CustomUser.objects.get(pk=pk)
#     except CustomUser.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == "GET":
#         serializer = ProfileSerializer(instance)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         incoming_data = JSONParser.parse(request)
#         serializer = ProfileSerializer(instance, data=incoming_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=404)
#
#     elif request.method == "DELETE":
#         instance.delete()
#         return HttpResponse(status=204)
