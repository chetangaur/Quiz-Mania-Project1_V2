from django.urls import path
from . import views

urlpatterns = [
    path('Docker_B',views.Docker_B,name='Docker_B'),
    path('Docker_I',views.Docker_I,name='Docker_I'),
    path('Docker_A',views.Docker_A,name='Docker_A'),

    path('AWS_B',views.AWS_B,name='AWS_B'),
    path('AWS_I',views.AWS_I,name='AWS_I'),
    path('AWS_A',views.AWS_A,name='AWS_A'),

    path('Redhat_B',views.Redhat_B,name='Redhat_B'),
    path('Redhat_I',views.Redhat_I,name='Redhat_I'),
    path('Redhat_A',views.Redhat_A,name='Redhat_A'),

    path('Python_B',views.Python_B,name='Python_B'),
    path('Python_I',views.Python_I,name='Python_I'),
    path('Python_A',views.Python_A,name='Python_A'),

    path('Tensorflow_B',views.Tensorflow_B,name='Tensorflow_B'),
    path('Tensorflow_I',views.Tensorflow_I,name='Tensorflow_I'),
    path('Tensorflow_A',views.Tensorflow_A,name='Tensorflow_A'),

    path('ComputerVision_B',views.ComputerVision_B,name='ComputerVision_B'),
    path('ComputerVision_I',views.ComputerVision_I,name='ComputerVision_I'),
    path('ComputerVision_A',views.ComputerVision_A,name='ComputerVision_A'),

    path('Kubernetes_B',views.Kubernetes_B,name='Kubernetes_B'),
    path('Kubernetes_I',views.Kubernetes_I,name='Kubernetes_I'),
    path('Kubernetes_A',views.Kubernetes_A,name='Kubernetes_A'),

    path('ScikitLearn_B',views.ScikitLearn_B,name='ScikitLearn_B'),
    path('ScikitLearn_I',views.ScikitLearn_I,name='ScikitLearn_I'),
    path('ScikitLearn_A',views.ScikitLearn_A,name='ScikitLearn_A'),
]