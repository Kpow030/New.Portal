from datetime import datetime
from  django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostSearchForm, PostForm
from .filters import NewFilter



def index(request):
    News = Post.objects.all()
    return render(request, 'index.html', context={'Post': News})



def detail(request, slug):
    new = Post.object.get(slug__iexavt=slug)
    return render(request, 'detail.html', context={'new':new})



def post_list(request):
    page = int(request.GET.get('page', 1))
    per_page = 10
    start = (page - 1) * per_page
    end = start + per_page

    total_post = Post.objects.count()
    post_list = Post.objects.order_by('-create_at') [start:end]

    pagination_range = 5
    if page < pagination_range:
        start_page = 1



def news_search(request):
    form = PostSearchForm(request.GET)
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    date_after = request.GET.get('date_after')

    post_list = Post.objects.all()

    if query:
        post_list = post_list.filter(title__icontains=query)

    if category_id:
        post_list = post_list.filter(category__id=category_id)

    if date_after:
        try:
            date_after = datetime.strptime(date_after, '%Y-%m-%d')
            post_list = post_list.filter(created_at__gte=date_after)
        except ValueError:
            pass


    context = {
        'form': form,
        'post_list': post_list,
    }

    return render(request, 'news/search.html', context)

def new_list(request):
    news_filter = NewFilter


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 13
        post.save()
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/update.html'


    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 18
        post.save()
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/news/'
    template_name = 'news/delete.html'

# Create your views here.
