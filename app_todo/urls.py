from rest_framework import routers

from . import views
app_name = 'app_todo'

router = routers.DefaultRouter()
router.register(r'todo', views.TodoViewSet)

urlpatterns = [

]