from django.urls import path,include
from app.views import show,detail
from app.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'viewlist',PersonViewSet,basename='viewlist')
router.register(r'teamlist',TeamViewSet,basename='teamlist')
router.register('tmz',Teamsviewset,basename='tmz')
router.register('demoauth',DemoAuthBasic,basename='demoauth')
# router.register(r'team',team,basename='team')
urlpatterns = [
    path('show/',show,name='show'),
    path('detail/',detail,name='detail'),
    path('superperson/',SuperPerson.as_view(),name='superperson'),
    path('demo/',DemoList.as_view(),name='demo'),
    path('demo/<int:pk>/',DemolistRUD.as_view(),name='demo'),
    path('demoapi/',DemoApi.as_view(),name='demoapi'),
    path('demoapi/<int:pk>/',DemoAPIRUD.as_view(),name='demoapi'),
    path('',include(router.urls)),
]
