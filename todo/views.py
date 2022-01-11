from django.shortcuts import render, redirect
from todo.models import Todo
from django.http import Http404
from todo.models import Memo
from django.utils import timezone

#ToDo
def home(request):
    """Todoリスト表示"""
    todo_lists = Todo.objects.all()
    data = {'todo_lists': todo_lists}
    return render(request, 'todo/home.html', data)

def create(request):
    """"Todoリスト追加"""
    if request.method == 'POST':
        todo_list = Todo.objects.create(
            title = request.POST['title'],
            detail = request.POST['detail'],
            created = request.POST['created'],
            map = request.POST['map'],
            now_time = timezone.datetime.now(),
        )
        return redirect('home')
    return render(request, 'todo/home.html')

def update(request, todo_list_id):
    """"Todoリスト編集"""
    todo_list = Todo.objects.get(pk=todo_list_id)
    if request.method == "POST":
        todo_list.title = request.POST.get('title')
        todo_list.detail = request.POST.get('detail')
        todo_list.created = request.POST.get('created')
        todo_list.map = request.POST.get('map')
        todo_list.now_time = timezone.datetime.now()
        todo_list.save()
        return redirect('home')
    todo_list = Todo.objects.get(pk=todo_list_id)
    data = {'todo_list': todo_list}
    return render(request, 'todo/update.html', data)

def delete(request, todo_list_id):
    """Todoリスト削除"""
    try:
        todo_list = Todo.objects.get(pk=todo_list_id)
    except Todo.DoesNotExist:
        raise Http404("Diary does not exist")
    
    todo_list.delete()
    return redirect('home')

#Memo
def memo(request):
    """"Memoリスト表示"""
    memo_lists = Memo.objects.all()
    data = {'memo_lists': memo_lists}
    return render(request, 'todo/memo.html', data)

def memo_create(request):
    """"Memoリスト追加"""
    if request.method == 'POST':
        memo_list = Memo.objects.create(
            text = request.POST['text'],
            time = timezone.datetime.now(),
        )
        return redirect('memo')
    return render(request, 'todo/memo.html')

def memo_delete(request, memo_list_id):
    """Todoリスト削除"""
    try:
        memo_list = Memo.objects.get(pk=memo_list_id)
    except Modo.DoesNotExist:
        raise Http404("Diary does not exist")
    
    memo_list.delete()
    return redirect('memo')

def hand(request):
    memo_lists = Memo.objects.all()
    data = {'memo_lists': memo_lists}
    return render(request, 'todo/hand.html', data)