from pyexpat import model
from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from app.models import Customers,Product,OrderedPlaced

class registratioForm(UserCreationForm):
    username= forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1= forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='Confirm password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email= forms.EmailField(required=True,label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    #is_staff= forms.BooleanField(required=True,label='Vendor',widget=forms.CheckboxInput(attrs={'class':'form-control'}))
    is_staff = forms.BooleanField(
        label="If You Vendor Check This Box",
        required=False,
        help_text="Check this box if the user is a staff member."
    )

    class Meta:
        model = User
        fields = ['username','email','is_staff','password1','password2',]

class LoginForm(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'})) 
    password= forms.CharField(label=_("Password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"),strip = False, widget= forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"),strip = False, widget= forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
        help_text=password_validation.
        password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"),strip = False, widget= forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email= forms.EmailField(label='Email',max_length=250, widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"),strip = False, widget= forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
        help_text=password_validation.
        password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"),strip = False, widget= forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['name','location','city','phone','provience','zipcode','email']

        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
        'location':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'provience':forms.Select(attrs={'class':'form-control'}),
        'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
        'phone':forms.NumberInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'})}
class ProductUploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','shopname','owner_email','selling_price','discount_price','description','brand','category','subcategory','product_image_frontside','product_image_backside','product_image_topside','product_image_bottomside','product_image_leftside','product_image_rightside']
        labels = {
            'title':'Product-Name'
        }
        widgets = {
                  'title':forms.TextInput(attrs={'class':'form-control'}),
                  'shopname':forms.TextInput(attrs={'class':'form-control'}),
                  'owner_email':forms.EmailInput(attrs={'class':'form-control'}),
                  'selling_price':forms.NumberInput(attrs={'class':'form-control'}),
                  'discount_price':forms.NumberInput(attrs={'class':'form-control'}),
                  'description': forms.Textarea(attrs={'class':'form-control'}),
                  'brand':forms.TextInput(attrs={'class':'form-control'}),
                  'category':forms.Select(attrs={'class':'form-control'}),
                  'subcategory':forms.TextInput(attrs={'class':'form-control'}),
                  'product_image_frontside':forms.ClearableFileInput(attrs={'placeholder': 'Enter image description','class':'form-control'}),
                  'product_image_backside':forms.ClearableFileInput(attrs={'required': False,'placeholder': 'Enter image description','class':'form-control'}),
                  'product_image_topside':forms.ClearableFileInput(attrs={'required': False,'placeholder': 'Enter image description','class':'form-control'}),
                  'product_image_bottomside':forms.ClearableFileInput(attrs={'required': False,'placeholder': 'Enter image description','class':'form-control'}),
                  'product_image_leftside':forms.ClearableFileInput(attrs={'required': False,'placeholder': 'Enter image description','class':'form-control'}),
                  'product_image_rightside':forms.ClearableFileInput(attrs={'required': False,'placeholder': 'Enter image description','class':'form-control'})
                  }
        

class ProductSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Search'}))


