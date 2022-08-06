from rest_framework import serializers
from order.models import Order

 
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id',
                  'design',
                  'start_date',
                  'end_date',
                  'page_count',
                  'email',
                  'phone_number',
                  'content',
                  'created_at',
                  'updated_at',
                  )