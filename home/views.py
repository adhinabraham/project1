from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import destinaiton
from django.contrib import messages
from django.views.decorators.cache import cache_control


from home.models import destinaiton

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    print('hii')
    if request.session.has_key('key'): 
        dest1=destinaiton()
        dest1.name = 'mumbai'
        dest1.desc = ' the city  that never sleep'
        dest1.img='destination_1.jpg'
        dest1.pirce=700
        dest1.offer=True
        
        dest2=destinaiton()
        dest2.name = 'hyderbad'
        dest2.desc = ' first biriyani , next sherwani'
        dest2.img='destination_2.jpg'
        dest2.pirce=100 
        dest2.offer=True
        
        dest3=destinaiton()
        dest3.name = 'Kochi'
        dest3.desc = ' gods own country'
        dest3.img='destination_3.jpg'
        dest3.pirce=1000
        dest3.offer=True
        
        dests=[dest1,dest2, dest3]
        
        return render(request,'index.html',{'dests':dests})
    else:
        return render(request,'login.html')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.session.has_key('key'):
        return redirect(home) 
    else:
        return render(request,'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def checkval(request):
    emailadhin='adhinabraham2000@gmail.com'
    passwordadhin= '12345'
    val1=request.GET['Email']

    val2=request.GET['Password1']
    print("val2 :",val2)
   
    if val1 == emailadhin and val2 == passwordadhin:
        print("eaqual")
        request.session['key'] = True
        return redirect('home')
    else:
        messages.error(request,'username or password not correct')
        return redirect(login)
    
        
        # return render(request,'login.html')
        
@cache_control(no_cache=True, must_revalidate=True, no_store=True)      
def logout(request):
    del request.session['key']
    return redirect(login)
    
        
    
    
    


