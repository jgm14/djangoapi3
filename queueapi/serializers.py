from rest_framework import serializers

from .models import Guest, AllQueues, InQueue, Users


""" class CustomerSerializer(serializers.ModelSerializer):

  class Meta:
    model = Customer
    fields = (
      'first_name',
      'last_name',
      'customer_id',
      'phone_num',
      'email_add'
    ) """

class GuestSerializer(serializers.ModelSerializer):

  class Meta:
    model = Guest
    fields = (
      'guest_id',
    )

class AllQueuesSerializer(serializers.ModelSerializer):

  class Meta:
    model = AllQueues
    fields = (
      'queue_id',
      'user_id',
      'queue_name',
      'queue_desc',
      'estimated_wait',
    )

class InQueueSerializer(serializers.ModelSerializer):

  class Meta:
    model = InQueue
    fields = (
      'queue_id',
      'guest_id',
      'timestamp',
    )

class UsersSerializer(serializers.ModelSerializer):

  class Meta:
    model = Users
    fields = (
      'email',
      'userID',
      'password',
      'firstName',
      'lastName',
    )