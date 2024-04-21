from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Song, Choice
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request): # Displays song
    """
    Renders the band.html template with the latest song list.

    :param HttpRequest request: The HTTP request.
    :returns: The rendered template.
    :rtype: HttpResponse
    """
    latest_song_list = Song.objects.order_by('-pub_date')[:5]
    context = {'latest_song_list': latest_song_list}
    return render(request, "band/band.html", context)

def detail(request, song_id):
    """
    Renders the detail.html template with details of the specified song.

    :param HttpRequest request: The HTTP request.
    :param int song_id: The ID of the song.
    :returns: The rendered template.
    :rtype: HttpResponse
    :raises Http404: If the song with the specified ID does not exist.
    """
    try:
        song = Song.objects.get(pk=song_id)
    except Song.DoesNotExist:
        raise Http404("Song does not exist.")
    return render(request, 'band/detail.html', {'song': song})

def results(request, song_id):
    """
    Renders the results.html template with the results of the specified song.

    :param HttpRequest request: The HTTP request.
    :param int song_id: The ID of the song.
    :returns: The rendered template.
    :rtype: HttpResponse
    :raises Http404: If the song with the specified ID does not exist.
    """
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'band/results.html', {'song': song})

@login_required(login_url='user_auth:login')
def vote(request, song_id):
    """
    Handles user voting for a song choice and redirects to the results page.

    :param HttpRequest request: The HTTP request.
    :param int song_id: The ID of the song.
    :returns: The HTTP response redirecting to the results page.
    :rtype: HttpResponseRedirect
    :raises Http404: If the song with the specified ID does not exist.
    :raises KeyError: If the 'choice' POST parameter is missing.
    :raises Choice.DoesNotExist: If the choice with the specified ID does not exist.
    """
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
    """
    Renders the concert_location.html template.

    :param HttpRequest request: The HTTP request.
    :returns: The rendered template.
    :rtype: HttpResponse
    """
    return render(request, 'band/concert_location.html')

@login_required(login_url='user_auth:login')
def contact_details(request):
    """
    Renders the contact_details.html template.

    :param HttpRequest request: The HTTP request.
    :returns: The rendered template.
    :rtype: HttpResponse
    """
    return render(request, 'band/contact_details.html')