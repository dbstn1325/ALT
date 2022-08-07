from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser

from order.serializers import OrderSerializer
import phonenumbers




from rest_framework.response import Response
from order.models import Order

@api_view(['GET', 'POST', 'DELETE'])
def order_list(request):
    if request.method == 'GET':
        order = Order.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            order = order.filter(title__icontains=title)
        
        order_serializer = OrderSerializer(order, many=True)
        # object를 serialize 해주기 위해서 safe=False 해준다.
        return JsonResponse(order_serializer.data, safe=False)
        # return Response(order_serializer.data)

    return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def order_create(request):
    if request.method == 'POST':
        order_data = JSONParser().parse(request)
        order_serializer = OrderSerializer(data=order_data)
        # (JOSN화된) 데이터가 조건에 유효한 데이터라면,
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse(order_serializer.data, status=status.HTTP_201_CREATED) 

    return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 


@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    try: 
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return JsonResponse({'message': '존재하지 않는 주문목록 입니다.'}, status=status.HTTP_404_NOT_FOUND)         
    

    if request.method == 'GET': 
        order_serializer = OrderSerializer(order)
        return JsonResponse(order_serializer.data) 

    return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    




@api_view(['GET', 'PUT', 'DELETE'])
def order_update(request, pk):
    try: 
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return JsonResponse({'message': '존재하지 않는 주문목록 입니다.'}, status=status.HTTP_404_NOT_FOUND)         
    

    if request.method == 'PUT':
        order_data = JSONParser().parse(request) 
        order_serializer = OrderSerializer(order, data=order_data) 

        if order_serializer.is_valid(): 
            order_serializer.save() 
            return JsonResponse(order_serializer.data) 

    return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


@api_view(['GET', 'PUT', 'DELETE'])
def order_delete(request, pk):
    try: 
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return JsonResponse({'message': '존재하지 않는 주문목록 입니다.'}, status=status.HTTP_404_NOT_FOUND)         
        
    if request.method == 'DELETE':
        order.delete()
        return JsonResponse({'message': '성공적으로 삭제 되었습니다.'}, status=status.HTTP_204_NO_CONTENT)   

    return JsonResponse({'message': '잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)     


