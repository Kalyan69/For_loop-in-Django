from django.shortcuts import render

# Create your views here.

def my_view(request):
    my_list = [1,2,3,4,5,6,7,8]
    my_name = 'Hello Developer'
    my_data = [('Kalyan',25),('preetam',10)]
    return render(request,'index.html',{"my_list":my_list,'xyz':my_name,'abc':my_data})