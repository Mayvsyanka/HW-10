from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import TagForm, QuoteForm, AuthorForm
from django.contrib.auth.decorators import login_required

from .mongo_models import Quote as Q, Author as A
from .models import Tag, Author, Quote
from .utils import connection
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
    View,

)

def main(request, page=1):
    quotes = Q.objects()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render (request, 'quotes/index.html', context={"quotes":quotes_on_page})

def author_info(request, _id):

    author = A.objects.get(pk=_id)
    return render(request, "quotes/author_info.html", {"author": author})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/author.html', {'form': form})

    return render(request, 'quotes/author.html', {'form': AuthorForm()})

@login_required
def add_quote(request):
    tags = Tag.objects.all()


    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/quote.html', {"tags": tags, 'form': form})

    return render(request, 'quotes/quote.html', {"tags": tags, 'form': QuoteForm()})

