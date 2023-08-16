from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import SignupForm, LoginForm, NewSubscriptionForm
from reviews_app.models import Review, UserFollows
from tickets_app.models import Ticket


def index(request, *args, **kwargs):
    context = {}
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        # if form.is_valid :
        user = authenticate(request, username=username, password=password)
        print(user)
        # if form.is_valid :
        if user:
            print("valid form")
            login(request, user)
            return redirect("homepage")
        else:
            print("invalid form")
            return redirect("index")

    else:
        # form = LoginForm()
        form = AuthenticationForm()
        context["form"] = form
        return render(request, "lit_reviews/index.html", context=context)


def signup(request, *args, **kwargs):
    context = {}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("valid form")
            form.save()
            return redirect("index")

        else:
            print("invalid form")
            return redirect("signup")
    else:
        # form = SignupForm()
        form = UserCreationForm()
        context["form"] = form
        return render(request, "lit_reviews/signup.html", context=context)


@login_required
def homepage(request, *args, **kwargs):
    context = {}

    subscriptions = UserFollows.objects.filter(user=request.user)
    subscriptions_ids = [sub.followed_user for sub in subscriptions]
    users_all = subscriptions_ids + [request.user]
    # print(users_all)
    all_tickets_with_reviews = Review.objects.values_list("ticket", flat=True)

    reviews_users_all = Review.objects.filter(user__in=users_all).order_by(
        "-time_created"
    )
    tickets_users_all = (
        Ticket.objects.exclude(pk__in=all_tickets_with_reviews)
        .filter(user__in=users_all)
        .order_by("-time_created")
    )

    context["reviews"] = reviews_users_all
    context["tickets"] = tickets_users_all

    """ if kwargs.get("message"):
        messages.info(request, message=kwargs.get("message")) """

    return render(request, "lit_reviews/homepage.html", context=context)


def follow_new_user(request):
    if request.method == "POST":
        user_username = request.user.username
        subs_username = request.POST.get("new-subscription")
        user = User.objects.get(username=user_username)
        subs_exists = User.objects.filter(username=subs_username).exists()

        if subs_exists:
            subs = User.objects.get(username=subs_username)
            UserFollows.objects.create(followed_user_id=subs.pk, user_id=user.pk)
            return redirect("homepage")

        else:
            return redirect("homepage", message="Ce nom d'utilisateur est incorrect")


def unfollow_user(request, subs_username):
    user_name = request.user.username
    user = User.objects.get(username=user_name)
    followed_user = User.objects.get(username=subs_username)
    user_subcription = UserFollows.objects.filter(
        user=user.pk, followed_user=followed_user.pk
    )
    user_subcription.delete()
    return redirect("subscriptions")


@login_required
def subscriptions(request):
    context = {}
    if request.method == "POST":
        user_username = request.user.username
        subs_username = request.POST.get("new-subscription")
        user = User.objects.get(username=user_username)
        subs_exists = User.objects.filter(username=subs_username).exists()

        if subs_exists:
            subs = User.objects.get(username=subs_username)
            UserFollows.objects.create(followed_user_id=subs.pk, user_id=user.pk)
            return redirect("subscriptions")

        else:
            return redirect(
                "homepage",
            )
    else:
        # form = NewSubscriptionForm()
        user = User.objects.get(username=request.user.username)
        followers_objects = UserFollows.objects.filter(followed_user=user.pk)
        followers = [record.user for record in followers_objects]

        followed_users_objects = UserFollows.objects.filter(user=user.pk)
        followed_users = [record.followed_user for record in followed_users_objects]

        # context["form"] = form
        context["followed_users"] = followed_users
        context["followers"] = followers
        print(context)
        return render(request, "lit_reviews/user_follows.html", context=context)


@login_required
def posts(request):
    reviews = Review.objects.filter(user=request.user).order_by("-time_created")
    tickets = Ticket.objects.filter(user=request.user).order_by("-time_created")
    context = {"reviews": reviews, "tickets": tickets}
    # print(context, request.user)
    return render(request, "lit_reviews/posts.html", context=context)


def logout_view(request):
    logout(request)
    return redirect("index")
