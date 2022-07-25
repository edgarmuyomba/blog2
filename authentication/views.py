from django.shortcuts import render, redirect
from django.views.generic import View 
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

class LoginPageView(View):
    template_name = 'authentication/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, {'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                message = 'You have been logged in successfully!'
                login(request, user)
                return redirect('core:home')
        message = 'Login Failed!'
        context = {'form': form, 'message': message}
        return render(request, self.template_name, context)

def LogoutPageView(request):
    logout(request)
    return redirect('authentication:login')

class SignUpPageView(View):
    template_name = 'authentication/signup.html'
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        message = ''
        context = {'form': form, 'message': message}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            role = request.POST['role']
            if role == 'Blogger':
                groupname = get_object_or_404(Group, name='Blogger')
                user.groups.add(groupname)
            else:
                groupname = get_object_or_404(Group, name='Reader')
                user.groups.add(groupname)
            login(request, user)
            return redirect('core:home')
        message = 'invalid details'
        context = {'form': form, 'message': message}
        return render(request, self.template_name, context)