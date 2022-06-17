from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Notes

# Create your views here.

# create a view to list all the notes

class NotesListView(ListView):
    model = Notes                                    # add the model you are listing objects from
    context_object_name = "notes"                   # what the view is expecting to receive --> notes
    template_name = "notes/notes_list.html"

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes' : all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         return render(request, 'notes/404Exception.html', {'pk' : pk})
#     return render(request, 'notes/notes_detail.html', {'note' : note})