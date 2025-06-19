from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import AddChildForm
from .models import FamilyGroup, Child


@login_required
def add_child(request):
    if not getattr(request.user, "is_parent", False) and not getattr(request.user, "is_guardian", False):
        return redirect("/")

    if request.method == "POST":
        form = AddChildForm(request.POST)
        if form.is_valid():
            child_user = User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            family, _ = FamilyGroup.objects.get_or_create(parent=request.user)
            Child.objects.create(
                family=family,
                name=form.cleaned_data["name"],
                user=child_user,
            )
            return redirect("/")
    else:
        form = AddChildForm()

    return render(request, "addfamily/add_child.html", {"form": form})
