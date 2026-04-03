from .models import Item, Claim
from .forms import ClaimForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ItemForm

@login_required
def report_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.reported_by = request.user
            item.save()
            return render(request, "success.html", {
                "message": "Your item has been reported successfully!"
            })
    else:
        form = ItemForm()

    return render(request, "report_item.html", {"form": form})

from .models import Item

from django.db.models import Q

def item_list(request):
    query = request.GET.get('q')
    items = Item.objects.all()

    if query:
        # This filters by name OR location
        items = items.filter(
            Q(name__icontains=query) |
            Q(location_found__icontains=query)
        )

    return render(request, 'item_list.html', {'items': items})


#add item using its id
from django.shortcuts import get_object_or_404
from .models import Item

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, "item_detail.html", {"item": item})

#claim form
@login_required
def claim_item(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == "POST":
        form = ClaimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.user = request.user
            claim.item = item
            claim.save()

            return render(request, "success.html", {
                "message": "Your claim has been submitted successfully!"
            })

    else:
        form = ClaimForm()

    return render(request, "claim_item.html", {"form": form, "item": item})

from django.contrib.auth.decorators import login_required

@login_required
def my_claims(request):
    claims = Claim.objects.filter(user=request.user)
    return render(request, "my_claims.html", {"claims": claims})

from django.contrib.auth.decorators import user_passes_test

def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def all_claims(request):
    claims = Claim.objects.all()
    return render(request, "all_claims.html", {"claims": claims})

#craete a sign up system
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})