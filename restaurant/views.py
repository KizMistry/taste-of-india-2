from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Meal
from .forms import ReviewForm
from django.http import HttpResponseRedirect


# Create your views here.

class Nav(View):

    def about(request):
        return render(request, "about.html")

    def book(request):
        return render(request, "book.html")

    def meals(request):
        return render(request, "meal.html")


class PostList(generic.ListView):
    model = Meal
    queryset = Meal.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6


class MealDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Meal.objects.filter(status=1)
        meal = get_object_or_404(queryset, slug=slug)
        comments = meal.comments.filter(approved=True).order_by('created_on')
        liked = False
        if meal.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "meal_detail.html",
            {
                "meal": meal,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "review_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Meal.objects.filter(status=1)
        meal = get_object_or_404(queryset, slug=slug)
        comments = meal.comments.filter(approved=True).order_by('created_on')
        liked = False

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            comment = review_form.save(commit=False)
            comment.meal = meal
            comment.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            "meal_detail.html",
            {
                "meal": meal,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "review_form": ReviewForm()
            },
        )


class MealLike(View):

    def post(self, request, slug):
        meal = get_object_or_404(Meal, slug=slug)

        if meal.likes.filter(id=request.user.id).exists():
            meal.likes.remove(request.user)
        else:
            meal.likes.add(request.user)

        return HttpResponseRedirect(reverse('meal_detail', args=[slug]))
