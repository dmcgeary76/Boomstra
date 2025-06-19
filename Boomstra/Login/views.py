from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect


def login_view(request):
    """Render and process a basic login form."""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
        return render(request, "Login/login.html", {"error": "Invalid credentials"})

    return render(request, "Login/login.html")
