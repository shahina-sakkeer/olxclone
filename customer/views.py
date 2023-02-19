from django.shortcuts import render,redirect
from customer.forms import RegistrationForm,LoginForm,UserForm,ProductForm
from django.views.generic import CreateView,FormView,TemplateView,ListView,View,DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from olx.models import UserProfile,User,Products,Category

# Create your views here.
class SignUpView(CreateView):
    template_name="signup.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("signin")

    def form_valid(self,form):
        messages.success(self.request,"account successfully created")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,"account creation failed")
        return super().form_invalid(form)


class LoginView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pswd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pswd)
            if usr:
                login(request,usr)
                return redirect("home-list")
            else:
                messages.error(self.request,"invalid credentials")
                return render(request,"login.html",{"form":form})

class UserProfileView(CreateView):
    template_name="user-profile.html"
    form_class=UserForm
    success_url=reverse_lazy("user-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"New profile is created")
        return super().form_valid(form)

class NavView(TemplateView):
    template_name="base.html"


class ProfileView(TemplateView):
    template_name="profile-view.html"
    form_class=UserForm
    

    def post(self,request,*args,**kwargs):
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
        else:
            messages.error(self.request,"invalid profile")
            return render(request,"base.html",{"form":form})

class ProductAddView(CreateView):
    template_name="product-add.html"
    form_class=ProductForm
    success_url=reverse_lazy("home-list")

    
    def form_valid(self, form):
        form.instance.owner=self.request.user
        messages.success(self.request,"New product is added")
        return super().form_valid(form)          

class HomeView(ListView):
    categories=Category.objects.all()
    template_name="product-list.html"
    context_object_name="product","category"
    model=Products

class DetailView(DetailView):
    template_name="product-detail.html"
    context_object_name="product"
    pk_url_kwarg="id"
    model=Products

class ProductDeleteView(View):
    def get(self,request,*args,**kw):
        id=kw.get("id")
        Products.objects.filter(id=id).delete()
        return redirect("home-list")
        messages.success(self.request,"deleted")


class OrderView(TemplateView):
    template_name="checkout.html"

    def get(self,request,*args,**kw):
        pid=kw.get("pid")
        qs=Products.objects.get(id=pid)
        return render(request,"checkout.html",{"product":qs})

def sign_out(request,*args,**kw):
    logout(request)
    return render("signin")  
          




            

        



    

    
    
    
    
      

            
    


    


    

