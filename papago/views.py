from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Question, Answer, Comment
from .forms import QuestionForm, AnswerForm, CommentForm

# Create your views here.

def index(request):
    """목록 출력"""
    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-create_date')
    
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list' : page_obj}

    return render(request, 'papago/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {'question' : question}

    return render(request, 'papago/question_detail.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    """답변 등록"""
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()

            return redirect('papago:detail', question_id=question.id)

    else:
        form = AnswerForm()

    context = {'question': question, 'form': form}

    return render(request, 'papago/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()

            return redirect('papago:index')

    else:
        form = QuestionForm()

    context = {'form': form}

    return render(request, 'papago/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    """ 질문수정 """
    question = get_object_or_404(Question, pk=question_id)
    
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('papago:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            
            return redirect('papago:detail', question_id=question.id)
    
    else:
        form = QuestionForm(instance=question)
    
    context = {'form': form}
    
    return render(request, 'papago/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """ 질문삭제 """
    question = get_object_or_404(Question, pk=question_id)
    
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        
        return redirect('papago:detail', question_id=question.id)
    
    question.delete()
    
    return redirect('papago:index')

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """ 답변수정 """
    answer = get_object_or_404(Answer, pk=answer_id)
    
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        
        return redirect('papago:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            
            return redirect('papago:detail', question_id=answer.question.id)
    
    else:
        form = AnswerForm(instance=answer)
    
    context = {'answer': answer, 'form': form}
    
    return render(request, 'papago/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """ 답변삭제 """
    answer = get_object_or_404(Answer, pk=answer_id)
    
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    
    else:
        answer.delete()
    
    return redirect('papago:detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    """ 질문댓글등록 """
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            
            return redirect('papago:detail', question_id=question.id)
    
    else:
        form = CommentForm()
    
    context = {'form': form}
    
    return render(request, 'papago/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    """ 질문댓글수정 """
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        
        return redirect('papago:detail', question_id=comment.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            
            return redirect('papago:detail', question_id=comment.question.id)
    
    else:
        form = CommentForm(instance=comment)
    
    context = {'form': form}
    
    return render(request, 'papago/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    """ 질문댓글삭제 """
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        
        return redirect('papag:detail', question_id=comment.question_id)
    
    else:
        comment.delete()
    
    return redirect('papago:detail', question_id=comment.question_id)

@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    """ 답글댓글등록 """
    answer = get_object_or_404(Answer, pk=answer_id)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('papago:detail', question_id=comment.answer.question.id)
    
    else:
        form = CommentForm()
    
    context = {'form': form}
    
    return render(request, 'papago/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    """ 답글댓글수정 """
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('papago:detail', question_id=comment.answer.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            
            return redirect('papago:detail', question_id=comment.answer.question.id)
    
    else:
        form = CommentForm(instance=comment)
    
    context = {'form': form}
    
    return render(request, 'papago/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    """ 답글댓글삭제 """
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        
        return redirect('papago:detail', question_id=comment.answer.question.id)
    
    else:
        comment.delete()
    
    return redirect('papago:detail', question_id=comment.answer.question.id)