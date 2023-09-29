from django.shortcuts import render, redirect, get_object_or_404, reverse
from ..users.models import CustomUser
from .models import CanditeForm
from .forms import CreateCandiForm, CanditeFormEditForm


def homePage(request):

    return render(request, "golosApp/index.html")

def candidatePage(request):
    users = CanditeForm.objects.all
    return render(request, "golosApp/candidates.html", {
        'users': users
    })

def candidateForm(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    userpop = CanditeForm.objects.all()
    userpop2 = []

    for j in userpop:
        if str(j.candidate) == str(user.username):
            userpop2.append(j)

    found_match = False
    for us in userpop:
        if str(us.candidate) == str(user.username):
            found_match = True
            break

    context = {
        'userpop': userpop,
        'found_match': found_match,
        'user': user,
        'userpop2':userpop2
    }

    return render(request, "golosApp/canditateform.html", context)

def edit_candite_form(request, pk, user_id):
    candite_form = get_object_or_404(CanditeForm, pk=pk)

    if request.method == 'POST':
        form = CanditeFormEditForm(request.POST, request.FILES, instance=candite_form)
        if form.is_valid():
            form.save()
            return redirect(reverse("golosApp:canditfr", args=[user_id]))
    else:
        form = CanditeFormEditForm(instance=candite_form)

    return render(request, 'golosApp/CanditChangeForm.html', {'form': form})

def createCandidateForm(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == "POST":
        form = CreateCandiForm(request.POST)
        if form.is_valid():
            candidate_form = form.save(commit=False)
            candidate_form.candidate = user
            candidate_form.save()
            return redirect(reverse("golosApp:canditfr", args=[user_id]))
    else:
        form = CreateCandiForm()

    return render(request, "golosApp/candformcr.html", {
        'form': form,
        'user': user,
    })
