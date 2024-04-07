from datetime import datetime

from django.contrib.auth.decorators import login_required
from  django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView


from .models import Post, Category
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


class CategoryList(ListView):
    model = Post
    template_name = 'news/category_list.html'
    context_object_name = 'category_news_list'


    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-date')
        return queryset


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context

@login_required
def subscribe(request, pk):
    user = request.user
    category = CategoryList.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписали на категории'
    return render(request, 'news/subscribe.html',{'category': category, 'message': message})
# Create your views here.
