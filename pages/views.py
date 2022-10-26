from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from orders.models import Order


class PizzaListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        query = Order.objects.get_or_create(customer=request.user)
        order = query[0]
        context = {
            'cart': order.getItemsCount()
        }
        return Response(data=context, template_name="pages/main.html")

def error_404(request, exception):
    return render(request, '404.html')
