from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Song, Choice
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request): # Displays song
    latest_song_list = Song.objects.order_by('-pub_date')[:5]
    context = {'latest_song_list': latest_song_list}
    return render(request, "band/band.html", context)

def detail(request, song_id):
    try:
        song = Song.objects.get(pk=song_id)
    except Song.DoesNotExist:
        raise Http404("Song does not exist.")
    return render(request, 'band/detail.html', {'song': song})

def results(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'band/results.html', {'song': song})

@login_required(login_url='user_auth:login')
def vote(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
        selected_choice = song.choice_set.get( pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'band/detail.html', {'song': song, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect( reverse('band:results', args=(song_id,)))
    
def concert_locations(request):
    return render(request, 'band/concert_location.html')

@login_required(login_url='user_auth:login')
def contact_details(request):
    return render(request, 'band/contact_details.html')