from django.shortcuts import render, redirect, get_object_or_404, Http404

# Create your views here.
from architecture.models import GenericAsset


def empty_navigate(request):
    assets = GenericAsset.objects.all()
    context = {'blank': True, 'assets': assets, 'src': None, 'dest': None}
    return render(request, 'navigation/nav.html', context)


def dest_navigate(request, dest):
    return redirect('navigation:full-navigate', '000', dest)


def navigate(request, source, dest):
    assets = GenericAsset.objects.all()
    if source == dest:
        return redirect('navigation:full-navigate', '000', dest)

    sources = GenericAsset.objects.filter(number=source)
    dests = GenericAsset.objects.filter(number=dest)

    if (not sources) or (not dests):
        raise Http404("Source or dest not found")

    src_room = sources[0]
    dest_room = dests[0]

    context = {'blank': False, 'src': src_room, 'dest': dest_room, 'assets': assets}
    return render(request, 'navigation/nav.html', context)
