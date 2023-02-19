from django.urls import path
from customer import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("register",views.SignUpView.as_view(),name="signup"),
    
    path("login",views.LoginView.as_view(),name="signin"),
    path("user/profile",views.UserProfileView.as_view(),name="profile"),
    path("home",views.NavView.as_view(),name="user-home"),
    path("profile/view",views.ProfileView.as_view(),name="profile"),
    path("products/add",views.ProductAddView.as_view(),name="product-create"),
    path("product/list",views.HomeView.as_view(),name="home-list"),
    path("product/details/<int:id>",views.DetailView.as_view(),name="product-detail"),
    path("product/delete/<int:id>",views.ProductDeleteView.as_view(),name="product-delete"),
    path("orders/add/<int:pid>",views.OrderView.as_view(),name="place-order"),
    path("logout",views.sign_out,name="signout")
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)