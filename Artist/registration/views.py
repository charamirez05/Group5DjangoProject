from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import ArtistForm, SingerForm, ActorForm, SoloArtistForm, GroupArtistForm


# Create your views here.

class HomeView(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)


class ArtistView(View):
    template = 'createArtist.html'

    def get(self, request):
        formArtist = ArtistForm()
        return render(request, self.template, {"formArtist": formArtist})

    def post(self, request):
        formArtist = ArtistForm(request.POST)
        isSinger = request.POST.get('isSinger', False)
        isActor = request.POST.get('isActor', False)
        if formArtist.is_valid():
            formArtist.save()
            if isSinger == 'on' and isActor == 'on':
                return redirect(reverse('registration:createNewSingerActor'))
            if isActor == 'on':
                return redirect(reverse('registration:createNewActor'))
            if isSinger == 'on':
                return redirect(reverse('registration:createNewSinger'))

        return render(request, self.template, {'formArtist': formArtist})


class SingerView(View):
    template = 'createSinger.html'

    def get(self, request):
        formSinger = SingerForm()
        return render(request, self.template, {'formSinger': formSinger})

    def post(self, request):
        formSinger = SingerForm(request.POST)
        isSolo = request.POST.get('isSolo', False)
        isGroup = request.POST.get('isGroup', False)
        if formSinger.is_valid():
            formSinger.save()
            return redirect(reverse('registration:index'))
        return render(request, self.template, {'formSinger': formSinger})

'''if isSolo == 'on' and isGroup == 'on':
                return redirect(reverse('registration:createSoloGroup'))
            if isGroup == 'on':
                return redirect(reverse('registration:createGroup'))
            if isSolo == 'on':
                return redirect(reverse('registration:createSolo'))'''

class ActorView(View):
    template = 'createActor.html'

    def get(self, request):
        formActor = ActorForm()
        return render(request, self.template, {'formActor': formActor})

    def post(self, request):
        formActor = ActorForm(request.POST)
        if formActor.is_valid():
            formActor.save()
            #return redirect(reverse('registration:index'))
        return render(request, self.template, {'formActor': formActor})


class SingerActorView(View):
    template = 'createNewSingerActor.html'

    def get(self, request):
        return render(request, self.template, {'formActor': ActorForm(), 'formSinger': SingerForm()})

    def post(self, request):
        formActor = ActorForm(request.POST)
        formSinger = SingerForm(request.POST)
        if formActor.is_valid() and formSinger.is_valid():
            formActor.save()
            formSinger.save()
            #return redirect(reverse('registration:index'))
        return render(request, self.template, {'formActor': ActorForm(), 'formSinger': SingerForm()})

class SoloArtistView(View):
    template = 'createSoloArtist.html'

    def get(self, request):
        formSoloArtist = SoloArtistForm()
        return render(request, self.template, {'formSoloArtist': formSoloArtist})

    def post(self, request):
        formSoloArtist = SoloArtistForm(request.POST)
        if formSoloArtist.is_valid():
            formSoloArtist.save()
            #return redirect(reverse('registration:index'))
        return render(request, self.template, {'formSoloArtist': formSoloArtist})


class GroupArtistView(View):
    template = 'createSoloArtist.html'

    def get(self, request):
        formGroupArtist = GroupArtistForm()
        return render(request, self.template, {'formGroupArtist': formGroupArtist})

    def post(self, request):
        formGroupArtist = GroupArtistForm(request.POST)
        if formGroupArtist.is_valid():
            formGroupArtist.save()
            #return redirect(reverse('registration:index'))
        return render(request, self.template, {'formGroupArtist': formGroupArtist})

class SoloGroupView(View):
    template = 'createSoloGroup.html'

    def get(self, request):
        return render(request, self.template, {'formSoloArtist': SoloArtistForm(), 'formGroupArtist': GroupArtistForm()})

    def post(self, request):
        formActor = ActorForm(request.POST)
        if formActor.is_valid():
            formActor.save()
            #return redirect(reverse('registration:index'))
        return render(request, self.template, {'formActor': formActor})




