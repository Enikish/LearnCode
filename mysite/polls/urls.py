from django.urls import path

from . import views

# path()包含四个参数，两个必填参数,route和view.两个可选参数kwargs和name
# route: 匹配URL的准则，当django响应请求时，会从urlpatterns的第一项开始进行匹配。顺序一次知道找到匹配的项。
# route不会匹配get和post参数或者域名。例如在请求127.0.0.1:8000/polls/index和127.0.0.1:8000/polls/index?page=3时，都只会匹配~/polls/index
# view: 当django找到匹配的url后，就会调用view这个特定的视图函数，并传入一个HttpRequest对象作为第一个参数，被捕获的参数以关键字参数的形式传入
app_name = "polls"  # 添加命名空间

# urlpatterns = [
#     # path("index", views.index),
#     path("recall", views.recall, name="recall"),
#     path("", views.index, name="index"),
#     path("<int:question_id>/results/", views.results, name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
#     path("detail/<int:question_id>/", views.detail, name="detail"),
# ]
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote")
]