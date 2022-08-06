from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from base.models import Administrator, Airline_Companie, Flight, Product,Customer,Countrie, Ticket, User_Role
from rest_framework import serializers
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from base.serializers import Airline_CompaniesSerializer, FlightsSerializer, ProductSerializer2, UserSerializer, ProductSerializer, CustomerSerializer,CountriesSerializer,AdministratorSerializer,User_RolesSerializer,TicketsSerializer,NoteSerializer
from rest_framework.response import Response
 
 
# from .serializers import NoteSerializer
from base.models import Note,User
 
 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        # ...
 
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 
 
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
 
    return Response(routes)
 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    print("innnn")
    user = request.user
    print(user)
    notes = user.note_set.all()
    print(notes)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


# register
@api_view(['POST'])
def addUser(request):
    try:
        User.objects.create_user(
            username=request.data["username"],
            email=request.data["email"],
            password=request.data["password"],
            # is_staff =request.data["is_staff"] ,
            # is_superuser =request.data["is_superuser"] 
            )
        return JsonResponse({"user_is_staff":"created!!!"} )

    except:
        return JsonResponse({"user_is_staff":"not created!!!"} )



        
 
 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addNote(request):
    print(request.data)
    user = request.user
    Note.objects.create(body=request.data["notebody"],user=user)
    print(user)
    notes = user.note_set.all()
    print(notes)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

# ---------------------------------------------------------------------------------------------------------------
def index(req):
    return JsonResponse('hello', safe=False)
 
# desc ,price,prodName,createdTime, _id
@api_view(['GET','POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def products(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return Response({
            "SINGLE-PROD":ProductSerializer2().get_Product_by_id(id),
            },status=status.HTTP_200_OK)

        else: 
            return Response({"ALL-PROD":ProductSerializer2().get_Product2()},safe=False) #return array as json response

    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        Product.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Product.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Product.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})
        # ------------------------------------------
        

    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        Product.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Product.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Product.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})



# ('id','first_name','last_name', 'address', 'phone_no', 'credit_card_no', 'user_id', 'createdTime')
@api_view(['GET','POST','DELETE','PUT'])
# @permission_classes([IsAuthenticated])
def customers(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-Customer":CustomerSerializer().get_Customers_by_id(id),
            },safe=False)

        else: 
            CustomerObj= Customer.objects.all()
            print(CustomerObj)
            return JsonResponse({"ALL-CUSTO":CustomerSerializer().get_Customers(CustomerObj)},safe=False) #return array as json response

    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        Product.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Product.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Product.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})



# ('id','country_name','image')
@api_view(['GET','POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def countries(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-Count":CountriesSerializer().get_Countries_by_id(id),
            },safe=False)

        else: 
            CountriesObj= Countrie.objects.all()
            return JsonResponse({"ALL-Countries":CountriesSerializer().get_Countries(CountriesObj)},safe=False) #return array as json response

    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        Product.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Product.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Product.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})



# ('id','status','first_name','last_name','user_id','createdTime')
@api_view(['GET','POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def administrators(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-Administrator":AdministratorSerializer().get_Administrator_by_id(id),
            },safe=False)

        else: 
            CountriesObj= Administrator.objects.all()
            print(CountriesObj)
            return JsonResponse({"ALL-Administrators":AdministratorSerializer().get_Administrators(CountriesObj)},safe=False) #return array as json response

    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        Administrator.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Administrator.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Administrator.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})



# ('id','status','company_name','country_id','user_id','createdTime')
@api_view(['GET','POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def Airline_Companies(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-Airline_Companies":Airline_CompaniesSerializer().get_Airline_Company_by_id(id),
            },safe=False)

        else: 
            CountriesObj= Airline_Companie.objects.all()
            print(CountriesObj)
            return JsonResponse({"ALL-Airline_Companies":Airline_CompaniesSerializer().get_Airline_Companies(CountriesObj)},safe=False) #return array as json response

    if request.method == 'POST': #method post add new row
        data =request.data
        # Airline_Companie.objects.create(Airline_CompaniesSerializer().add_new_Airline_Company(data))
        print({'POST':"test"})
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Airline_Companie.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Airline_Companie.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})

# Flight

# ('id','status','airline_company_id','origin_country_id','destination_country_id','departure_time','landing_time','remaining_tickets','createdTime')
@api_view(['GET','POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def flights(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-flights":FlightsSerializer().get_Flights_by_id(id),
            },safe=False)

        else: 
            CountriesObj= Flight.objects.all()
            print(CountriesObj)
            return JsonResponse({"ALL-flights":FlightsSerializer().get_Flights(CountriesObj)},safe=False) #return array as json response

    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        Flight.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Flight.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Flight.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})



# ('id','status','role_name','createdTime')
@api_view(['GET','POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def User_Roles(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-User_Role":User_RolesSerializer().get_User_Role_by_id(id),
            },safe=False)

        else: 
            CountriesObj= User_Role.objects.all()
            print(CountriesObj)
            return JsonResponse({"ALL-User_Roles":User_RolesSerializer().get_User_Roles(CountriesObj)},safe=False) #return array as json response

    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        User_Role.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= User_Role.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=User_Role.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})


# ('id','status','flight_id','costumer_id','createdTime')
@api_view(['GET','POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def Tickets(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE-Tickets":TicketsSerializer().get_Tickets_by_id(id),
            },safe=False)

        else: 
            CountriesObj= Ticket.objects.all()
            return JsonResponse({"ALL-Tickets":TicketsSerializer().get_Tickets(CountriesObj)},safe=False) #return array as json response

    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        Ticket.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Ticket.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Ticket.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})



