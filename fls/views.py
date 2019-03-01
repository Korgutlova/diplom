from django.shortcuts import render

from fls.forms import CompetitionForm
from fls.models import Param, Competition


def params(request):
    # hardcode
    comp = Competition.objects.get(name="Студент Года")

    if request.method == 'POST':
        print(request.POST.getlist('text'))
        for text, desc, min, max in zip(request.POST.getlist('text'), request.POST.getlist('description'),
                                        request.POST.getlist('min'),
                                        request.POST.getlist('max')):
            Param.objects.create(name=text, description=desc, min=min, max=max, competition=comp)
    return render(request, 'fls/add_params.html', {})


def criteria(request):
    # hardcode
    comp = Competition.objects.get(name="Студент Года").id

    params = Param.objects.filter(competition=comp)
    return render(request, 'fls/add_criteria.html', {"params": params})


def comp(request):
    form = CompetitionForm()
    if request.method == 'POST':
        form = CompetitionForm(request.POST)
        if form.is_valid():
            form.save()
            form = CompetitionForm()
    return render(request, 'fls/add_comp.html', {"form": form})