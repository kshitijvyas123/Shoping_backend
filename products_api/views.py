from django.http import HttpResponse,JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .RegisterSerializer import UserSerializer,RegisterSerializer
from .ProductsSerializer import ProductsSerilizar
from django.contrib.auth.models import User
from .models import AddProduct 


from django.contrib.auth import login , authenticate

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            response = HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
            response["Access-Control-Allow-Origin"] = "*"
            response["Content-Type"] = "application/json; charset=UTF-8"         
            
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        print(request.data);
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            if user.is_active:
                login(request, user)

                username1 = User.objects.get(username =user)
                data = {'data': {'name': user.username, 'email': user.email,'firstName':user.first_name,'lastName':user.last_name}, "message":{"Success"}}


                return Response(data=data,status=status.HTTP_200_OK)
            else:
                data = {"status":{"fail"},'message':{'wrong username/password.'}}
                return Response( data=data)
        else:
            data = {"status":{"fail"},'message':{'wrong username/password.'}}
            return Response( data=data)

@api_view([])
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
@api_view(['GET'])
def products_list(request):
    if request.method == 'GET':
        try:
            products = AddProduct.objects.all()
            serializer = ProductsSerilizar(products, many=True)
            # info = {"status":"pass", "message":"Success"}
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except:
            data = {"status":{"fail"},'message':{'Something went wrong.'}}
            return Response( data=data)
    
@api_view(['GET'])
def products_detail(request,pk):
    print("I am here---")
    try:
        products = AddProduct.objects.get(pk=pk)

    except AddProduct.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
       
        serializer = ProductsSerilizar(products, many=True)
        
        return JsonResponse(serializer.data, safe=False)
