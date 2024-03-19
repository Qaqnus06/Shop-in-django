from django .contrib.auth.models import User

from django  import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }

    def clean_username(self):
        username=self.cleaned_data['username']
        
        if len(username)<6 or len(username)>10:
            raise forms.ValidationError('Siz kiritgan username 5 va 10 uzunlikda bolishi kerak')
        return username
    
    def clean_password(self):
        password=self.cleaned_data['password']
        

        if len(password)<4  :
            raise forms.ValidationError('parol eng kamida 4 xonalik kiritasz')
      
        return password


        

class RegisterForm(forms.ModelForm):
    # password_confirm=forms.PasswordInput()

    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields['password_confirm']=forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model=User
        fields=['username','first_name' ,'last_name','email','password']

    def clean_password_confirm(self):
        password=self.cleaned_data['password']
        password_confirm=self.cleaned_data['password_confirm']    

        if password!=password_confirm:
            raise forms.ValidationError('parollar ikki hil bir biriga mos kelishi kerak')
        return password_confirm
    

    def clean_username(self):
        username=self.cleaned_data['username']

        if len(username)<5 or len (username)>30:
            raise forms.ValidationError('username 5 va 30 oraligida bolish kerak')
        
        return username
        
        