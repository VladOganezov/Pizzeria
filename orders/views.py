from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from menu.models import RegularPizza, SicilianPizza, Sub, Salad, Extra, Platter, Pasta, Topping
from orders.models import Order, OrderItem, Payment


class CartListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        query = Order.objects.get_or_create(customer=request.user)
        order = query[0]
        context = {
            'cart': order.getItemsCount(),
            'order': order
        }
        return Response(data=context, template_name="orders/cart.html")

class OrdersListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        query = Order.objects.get_or_create(customer=request.user)
        order = query[0]
        context = {
            "reg_pizza": RegularPizza.objects.all(),
            "sic_pizza": SicilianPizza.objects.all(),
            "pastas": Pasta.objects.all(),
            "subs": Sub.objects.all(),
            "extras": Extra.objects.all(),
            "platters": Platter.objects.all(),
            "salads": Salad.objects.all(),
            "toppings": Topping.objects.all().order_by('name'),
            'cart': order.getItemsCount()
        }
        return Response(data=context, template_name="orders/order_place.html")

    def post(self, request, *args, **kwargs):
        data = request.POST
        if data['form_name'] == 'reg_pizza':
            toppings = ' toppings - ' if data.getlist('reg_toppings').__len__() > 0 else ' '
            quantity = data['qty']
            name = f"{data['size'].title()} Regular Pizza - {data['pizza_name']}{toppings}{', '.join(Topping.objects.filter(id__in=data.getlist('reg_toppings')).values_list('name', flat=True))}"
            price = RegularPizza.objects.get(no_of_toppings=data['pizza_name']).__getattribute__(f"{data['size']}_price")

        query = Order.objects.get_or_create(customer=request.user)
        order = query[0]

        if order.items.filter(name=name).exists():
            item = order.items.get(name=name)
            item.quantity += int(quantity)
            item.save()
            request.session.__setitem__(
                'cart', order.getItemsCount()
            )
        else:
            item = OrderItem.objects.create(
                name=name, price=price, quantity=quantity
            )
            order.items.add(item)
            item.save()
            request.session.__setitem__(
                'cart', order.getItemsCount()
            )
        return Response(template_name="orders/order_place.html")
