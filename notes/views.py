from django.shortcuts import render, redirect,get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required


def mark_completed(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.is_completed = True
    note.save()
    print(f"Marked as completed: {note.title} → {note.is_completed}")
    return redirect('note_list')

def remove_task(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    print(f"Task removed: {note.title}")
    note.delete()
    return redirect('note_list')


@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-is_completed', '-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})








@login_required
def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Note.objects.create(user=request.user, title=title, content=content)
            return redirect('note_list')

    return render(request, 'notes/add_note.html')
