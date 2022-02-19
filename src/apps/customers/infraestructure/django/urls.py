from django.urls import path

import apps.customers.infraestructure.django.views as customer_views


routes = [
    path('customers/', customer_views.CustomersListAPIView.as_view()),
    path('customers/add/', customer_views.CustomersCreateAPIView.as_view()),
    # path('<int: customer_uuid>', customer_views.retrieve),
]