from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('start', start_page),
    path('', page_view, name='main'),
    path('wait', void_view),
    path('<int:page_id>', page_view),
    path('print/<int:page_id>/<int:button_id>', print_sticker, name="print"),
    path('operator/<int:operator_id>', operator_view),
    path('operator/without_ticket/<int:operator_id>', without_ticket),
    path('operator/ready/<int:operator_id>', ticket_ready),
    path('queue/<int:operator_id>', queue_view),
    path('queue', all_queue_view),
    path('expert/<int:expert_id>', expert_view),
    path('expert/ready/<int:expert_id>', expert_ticket_ready),
    path('expert/without_ticket/<int:expert_id>', expert_without_ticket)
]