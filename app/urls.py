from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm, MyPasswordResetForm,MySetPasswordForm
urlpatterns = [
    
    path('', views.ProductView.as_view(),name='home'),


    path('tool/',views.ToolView.as_view(),name = 'toolpage'),
    path('furniture/',views.FurnitureView.as_view(),name = 'furniturepage'),
    path('art/',views.ArtView.as_view(),name = 'artpage'),
    path('boy/',views.BoyfashionView.as_view(),name = 'boypage'),
    path('girl/',views.GirlfashionView.as_view(),name = 'girlpage'),
    path('man/',views.ManfashionView.as_view(),name = 'manpage'),
    path('woman/',views.WomanfashionView.as_view(),name = 'womanpage'),
    path('baby/',views.BabyView.as_view(),name = 'babypage'),
    path('electronics/',views.ElectronicsView.as_view(),name = 'electronicpage'),
    path('beauty/',views.BeautyView.as_view(),name = 'beautypage'),
    path('sport/',views.SportView.as_view(),name = 'sportpage'),
    path('toy/',views.ToysView.as_view(),name = 'toypage'),
    path('book/',views.BookView.as_view(),name = 'bookpage'),
    path('pet/',views.PetView.as_view(),name = 'petpage'),
    path('tool/',views.ToolView.as_view(),name = 'toolpage'),
    path('digital/',views.DigitalView.as_view(),name = 'digitalpage'),
    path('food/',views.FoodView.as_view(),name = 'foodpage'),
    path('automotive/',views.AutomotiveView.as_view(),name = 'automotivepage'),
    path('kitchen/',views.KitchenView.as_view(),name = 'kitchenpage'),
    path('groceries/',views.GroceriesView.as_view(),name = 'groceriespage'),


    path('product-detail/<int:pk>', views.product_detail.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.ShowCart, name='showcart'),
    path('plus-cart/', views.PlusCart),
    path('minus-cart/', views.MinusCart),
    path('remove-cart/', views.removecart, name='removecartpage'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),


    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    path('logout', views.LogoutView, name = 'logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='pc'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='pcdone'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm), name='passwordreset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class = MySetPasswordForm), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    path('registration/', views.customerregistrationform.as_view(), name='customerregistration'),

    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.PaymentDoneView,name='paymentdone'),
    path('productupload/', views.ProductUploadView.as_view(), name = 'productuploadpage'),

    path('search/', views.product_search, name='product_search'),
]