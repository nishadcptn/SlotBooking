from django.shortcuts import render
from Teachers.models import *
from Teachers.serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from datetime import datetime
# Create your views here.

#### -----Todays date ###

def Today():
    return datetime.date(datetime.today())

"""
    --------Get the Teacher from available teachers pool
"""
def getRandomTeachers(_slot):
    _bkd = booking.objects.filter(date__icontains=Today(),slot=_slot).values('teacher')
    _attn = attandance.objects.filter(p_in__icontains=Today(),is_active=True).values('teacher')
    available = [item for item in list(_attn) if item not in list(_bkd)]
    _teacher = random.choice(available)
    return _teacher

"""
    ------check the slot is available 
"""
def checkSlot(_slot):

    _teachers = attandance.objects.filter(p_in__icontains=Today(),is_active=True).count()

    _booking = booking.objects.filter(slot=_slot, date__icontains=Today()).count()
    
    if ( _teachers -_booking) >1:
        return True
    else:
        return False
    
"""
    ------Api to get the all teachers details
    ------Api to Create New Teaccher Credentials/Update 
"""
class TeacherApi(APIView):
    def get(self, req, pk=None):
        if pk is not None:
            _teacher = teacher.objects.get(id=pk)
            serializer = TeacherSerializer(_teacher)
            return Response(serializer.data)

        _teacher = teacher.objects.all()
        serializer = TeacherSerializer(_teacher,many=True)
        return Response(serializer.data)

    def post(self, req):
        serializer = TeacherSerializer(data = req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"success"})
        else:
            return Response(serializer.errors)

    def put(self, req, pk):
        _teacher = teacher.objects.get(id=pk)
        serializer = TeacherSerializer(_teacher, data = req.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"success"})
        else:
            return Response(serializer.errors)

""" 
    Punchin API 
    get : Teachers available today
    post: PUNCHIN WITH TEACHERS ID
        params - teacher: 1
"""

class AttandanceApi(APIView):
    def get(self, req):
        _att_data = attandance.objects.filter(p_in__icontains=Today())
        serializer = AttnSerializer(_att_data, many=True)
        return Response(serializer.data)

    def post(self, req):
        serializer = AttnSerializer(data = req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"success"})
        else:
            return Response(serializer.errors)

""" 
    PunchOut API 
    post: PUNCHOUT WITH TEACHERS ID
        params - id: 1
"""
class Punchout(APIView):
    def post(self, req):
        _id = req.data['id']
        _teacher = attandance.objects.filter(teacher=_id,p_in__icontains=Today(),is_active=True)

        if not teacher:

            return Response ({
                'msg': 'Attendance Not available'
            })

        else:
            _data = {
                'p_out': datetime.today(),
                'is_active': False
            }
            serializer = AttnSerializer(_teacher[0], data = _data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':"success"})
            else:
                return Response(serializer.errors)


"""
    SLOTS API
    (Only for creating and displaying slot)
    POST:
    create slot
    params - slot:"10:30"

"""
class SlotsApi(APIView):
    def get(self, req):
        _slots = slots.objects.all()
        serializer = SlotSerializer(_slots, many=True)
        return Response(serializer.data)

    def post(self, req):
        serializer = SlotSerializer(data = req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"success"})
        else:
            return Response(serializer.errors)

"""
    To Check available Slots Today 
    get:
        returns slot and its status
    
"""
class AvailableSlots(APIView):
    def get(self, req):

        Slot_details={}
        slot_tbl = slots.objects.all()
        _teachers = attandance.objects.filter(p_in__icontains=Today(),is_active=True).count()

        for x in slot_tbl:

            _booking = booking.objects.filter(slot=x, date__icontains=Today()).count()
            if ( _teachers -_booking) >1:
                Slot_details[x.slot]=True
            else:
                Slot_details[x.slot]=False

        return Response(Slot_details)

"""
    To Book available Slots Today 
    POST:
       params - 'id' : 1, 'slot' : "02:30"
    
"""

class BookingApi(APIView):
    def post(self, req):

        _slot = req.data.get('slot')
        std_id = req.data.get('id')

        if(checkSlot(_slot)):
            _userBooked = booking.objects.filter(student=std_id,date__icontains=Today())
            if _userBooked:
                response = {'msg':"Alredy Booked a slot Today"}
                return Response(response)
            else:
                _teacher = getRandomTeachers(_slot)

                _data = {
                    'student': std_id,
                    'teacher' : _teacher['teacher'],
                    'slot' : _slot
                }
                serializer = BookingSerializer(data = _data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg':"success"})
                else:
                    return Response(serializer.errors)
        else:
            return Response({'msg':"! Slot unavailable"})