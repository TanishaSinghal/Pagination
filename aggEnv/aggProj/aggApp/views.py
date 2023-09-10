import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.db import connection

from .models import Student
from .serializers import *
from .constants import *

@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def students_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
   
@api_view(['GET', 'POST']) 
def paginate(request): 
    
    template = loader.get_template('pagination.html')
    
    current_page = int(request.GET.get("page", "1"))
    dir = str(request.GET.get("dir", "None"))
    sort = request.GET.get("sort", "name")
    search = request.GET.get("search", "")
    print("search", search)

    current_slot = math.ceil(current_page / NUMBER_OF_PAGE_LINKS_PER_SLOT)
    
    ############## calculating other dependant variables ###################
    
    total_records = Student.objects.all().count()
    number_of_pages = math.ceil(total_records/RECORD_PER_PAGE)
    number_of_slots = math.ceil(number_of_pages / NUMBER_OF_PAGE_LINKS_PER_SLOT)
    
    limit = RECORD_PER_PAGE
    offset = (current_page - 1) * RECORD_PER_PAGE    
    # all_page_data = Student.objects.all()[offset:offset+limit]
    
    message = ''
    
    ############## calculating prev ###################
    
    if current_slot > 1:
        prev = (current_slot-1) * NUMBER_OF_PAGE_LINKS_PER_SLOT
    else: 
        prev = None
        message = "prev slot does not exist"
        
    ############## calculating next ###################
        
    if  current_page <= ((number_of_slots -1) * NUMBER_OF_PAGE_LINKS_PER_SLOT):    
        next = current_slot * NUMBER_OF_PAGE_LINKS_PER_SLOT + 1        
    elif ((number_of_slots -1) * NUMBER_OF_PAGE_LINKS_PER_SLOT +1) <= current_page <= number_of_pages:
        next = None
        message = "next slot does not exist"
    elif current_page > number_of_pages : 
        next = None
        message = "page you are looking for does not exist"
        
    ############## setting sorting direc ########################
    
    if dir == "ascending":
        sorted_data = Student.objects.all().values().order_by(sort)[offset:offset+limit]
        
    elif dir == "descending":
        sorted_data = Student.objects.all().values().order_by(sort)[::-1][offset:offset+limit]
    else:
        sorted_data = Student.objects.all().values()[offset:offset+limit]
        
    all_page_data = sorted_data[offset:offset+limit]
        
    ##################### context ############################
    
    
    context = {
        'prev' : prev,
        'next' : next,
        'pages_in_slot' : NUMBER_OF_PAGE_LINKS_PER_SLOT,
        'total_records' : total_records,
        'number_of_pages' : number_of_pages,
        'number_of_pages_loop' : range((current_slot - 1) * NUMBER_OF_PAGE_LINKS_PER_SLOT + 1 ,min(number_of_pages, current_slot * NUMBER_OF_PAGE_LINKS_PER_SLOT) +1 ),
        'number_of_slots' : number_of_slots,
        'all_page_data' : sorted_data,
        'current_page' : current_page, 
        'current_slot' : current_slot,  
        'message' : message,   
        'dir' : dir,  
        'sort' : sort,  
        'search' : search,
    }
    
    context_api = [NUMBER_OF_PAGE_LINKS_PER_SLOT, total_records, number_of_slots,current_page,current_slot,dir,sort, number_of_pages,sorted_data]
    return Response(context_api) if request.path.startswith(URL_PREFIX) else HttpResponse(template.render(context, request))    