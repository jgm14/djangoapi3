from django.shortcuts import get_object_or_404
from django.shortcuts import render
import operator

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Guest, AllQueues, InQueue, Users
from .serializers import  GuestSerializer, AllQueuesSerializer, InQueueSerializer, UsersSerializer


""" class CustomerView(APIView):
    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the Todo item by that id
            try:
                # Check if the todo item the user wants to update exists
                queryset = Customer.objects.get(customer_id=id)
            except Customer.DoesNotExist:
                # If the todo item does not exist, return an error response
                return Response({'error': 'No customer with the given ID.'}, status=400)

            # Serialize todo item from Django queryset object to JSON formatted data
            read_serializer = CustomerSerializer(queryset)

        else:
            # Get all todo items from the database using Django's model ORM
            queryset = Customer.objects.all()

            # Serialize list of todos item from Django queryset object to JSON formatted data
            read_serializer = CustomerSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)
    
    def post(self, request):
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) """


class QueueView(APIView):
    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the Todo item by that id
            try:
                # Check if the todo item the user wants to update exists
                queryset = AllQueues.objects.get(user_id=id)
            except AllQueues.DoesNotExist:
                # If the todo item does not exist, return an error response
                return Response({'error': 'No queue with the given ID.'}, status=400)

            # Serialize todo item from Django queryset object to JSON formatted data
            read_serializer = AllQueuesSerializer(queryset)

        else:
            # Get all todo items from the database using Django's model ORM
            queryset = AllQueues.objects.all()

            # Serialize list of todos item from Django queryset object to JSON formatted data
            read_serializer = AllQueuesSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)

    def post(self, request):
        serializer = AllQueuesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, id=None):
        try:
        # Check if the todo item the user wants to update exists
            queue_entry = AllQueues.objects.get(user_id=id)
        except AllQueues.DoesNotExist:
            # If the todo item does not exist, return an error response
            return Response(AllQueuesSerializer.errors)

        # If the todo item does exists, use the serializer to validate the updated data
        update_serializer = AllQueuesSerializer(queue_entry, data=request.data)

        # If the data to update the todo item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

            # Data was valid, update the todo item in the database
            queue_entry_object = update_serializer.save()

            # Serialize the todo item from Python object to JSON format
            read_serializer = AllQueuesSerializer(queue_entry_object)

        # Return a HTTP response with the newly updated todo item
        return Response(read_serializer.data)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors)
    
    def delete(self, request, id=None):
        try:
            # Check if the todo item the user wants to update exists
            queue_item = AllQueues.objects.get(user_id=id)
        except AllQueues.DoesNotExist:
            # If the todo item does not exist, return an error response
            return Response({'errors': 'No queue with the given ID.'}, status=400)

        # Delete the chosen todo item from the database
        queue_item.delete()

        # Return a HTTP response notifying that the todo item was successfully deleted
        return Response({'Success': 'Queue deleted.'},status=204)


class GuestView(APIView):
    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the Todo item by that id
            try:
                # Check if the todo item the user wants to update exists
                queryset = Guest.objects.get(guest_id=id)
            except Guest.DoesNotExist:
                # If the todo item does not exist, return an error response
                return Response({'error': 'No guest with the given ID.'}, status=400)

            # Serialize todo item from Django queryset object to JSON formatted data
            read_serializer = GuestSerializer(queryset)

        else:
            # Get all todo items from the database using Django's model ORM
            queryset = Guest.objects.all()

            # Serialize list of todos item from Django queryset object to JSON formatted data
            read_serializer = GuestSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)

    def post(self, request):
        serializer = GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id=None):
        try:
            # Check if the todo item the user wants to update exists
            guest_item = Guest.objects.get(guest_id=id)
        except Guest.DoesNotExist:
            # If the todo item does not exist, return an error response
            return Response({'errors': 'No guest with the given ID.'}, status=400)

        # Delete the chosen todo item from the database
        guest_item.delete()

        # Return a HTTP response notifying that the todo item was successfully deleted
        return Response({'Success': 'Guest deleted.'},status=204)


class InQueueView(APIView):
    def get(self, request, id=None):
        if id:
        # If an id is provided in the GET request, retrieve the Todo item by that id
            try:
                # Check if the todo item the user wants to update exists
                #queryset = InQueue.objects.all()
                queryset = InQueue.objects.filter(queue_id=id)
                sortedSet = sorted(queryset, key=operator.attrgetter('timestamp'))
                #print(queryset)
                #queryset = InQueue.objects.get(queue_id=id)
                #queryset = queryset.InQueue_set.all()  # retrieve all related HostData objects
            except InQueue.DoesNotExist:
                # If the todo item does not exist, return an error response
                return Response({'error': 'No queue with the given ID.'}, status=400)

            # Serialize todo item from Django queryset object to JSON formatted data
            read_serializer = InQueueSerializer(sortedSet, many=True)

        else:
            # Get all todo items from the database using Django's model ORM
            queryset = InQueue.objects.all()

            # Serialize list of todos item from Django queryset object to JSON formatted data
            read_serializer = InQueueSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)

    def post(self, request):
        serializer = InQueueSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id=None):
        try:
            # Check if the todo item the user wants to update exists
            InQueue_item = InQueue.objects.get(guest_id=id)
        except InQueue.DoesNotExist:
            # If the todo item does not exist, return an error response
            return Response({'errors': 'No queue with the given ID.'}, status=400)

        # Delete the chosen todo item from the database
        InQueue_item.delete()

        # Return a HTTP response notifying that the todo item was successfully deleted
        return Response({'Success': 'InQueue Instance deleted.'},status=204)


class UsersView(APIView):

    def get(self, request):
        _email = request.GET.get('email')
        _password = request.GET.get('password')
        if (_email and _password):
            try:
                queryset = Users.objects.get(email=_email , password=_password)
            except Users.DoesNotExist:
                return Response({'error': 'No user with the given credentials.'}, status=400)

            read_serializer = UsersSerializer(queryset)
            return Response(read_serializer.data)

        return Response({'error': 'Outside.'}, status=400)
        
    def post(self, request):
        serializer = UsersSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)    