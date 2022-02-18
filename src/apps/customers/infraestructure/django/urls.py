from django.urls import path

import customers.infraestructure.django.views as customer_views


routes = [
    path('', customer_views.CustomersListAPIView.as_view()),
    path('<int: customer_uuid>', customer_views.retrieve),
]