import json
from rest_framework import generics
from django.http import JsonResponse
from .models import PriceChange, Investment
from django.views import View
from .serializers import Karbarserialazers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.serializers import serialize




class Sod(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        alldata = PriceChange.objects.all()
        data = request.data
        start = data.get('start')
        end = data.get('end')
        many = data.get('many')
        fund = data.get('fund')

        starting = alldata.filter(fund__name=fund, month__name=start).first()
        ending = alldata.filter(fund__name=fund, month__name=end).first()

        if starting and ending:
            profit_percentage = (ending.price - starting.price) / starting.price * 100
            final_amount = int(many) * (1 + profit_percentage / 100)

            investment = Investment.objects.create(
                investor_id= request.user.id,
                fund=ending,
                initial_amount=int(many),
                start_month=start,
                end_month=end,
                profit=profit_percentage
            )
            return JsonResponse(final_amount, safe=False)

        return JsonResponse("not found", safe=False)


class ShowKarbar(generics.ListAPIView):
    queryset = Investment.objects.all()
    serializer_class = Karbarserialazers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Investment.objects.filter(investor=self.request.user)




import json
from rest_framework import generics
from django.http import JsonResponse
from .models import PriceChange, Investment
from django.views import View
from .serializers import Karbarserialazers
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class Sod(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        alldata = PriceChange.objects.all()
        data = request.data
        start = data.get('start')
        end = data.get('end')
        many = data.get('many')
        fund = data.get('fund')

        starting = alldata.filter(fund__name=fund, month__name=start).first()
        ending = alldata.filter(fund__name=fund, month__name=end).first()

        if starting and ending:
            profit_percentage = (ending.price - starting.price) / starting.price * 100
            final_amount = int(many) * (1 + profit_percentage / 100)

            Investment.objects.create(
                investor_id=request.user.id,
                fund=ending,
                initial_amount=int(many),
                start_month=start,
                end_month=end,
                profit=profit_percentage
            )
            return JsonResponse({'final_amount': final_amount})

        return JsonResponse({'error': "not found"}, status=404)

class ShowKarbar(generics.ListAPIView):
    queryset = Investment.objects.all()
    serializer_class = Karbarserialazers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Investment.objects.filter(investor=self.request.user)

@method_decorator(csrf_exempt, name='dispatch')
class Best(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        prices = PriceChange.objects.filter(fund__name=name)

        if not prices.exists():
            return JsonResponse({'error': "PriceChange not found for the given fund name"}, status=404)

        lis = [price.price for price in prices]
        max_diff, min_value, max_pair = self.calculate_max_difference(lis)

        start = prices.filter(price=max_pair[0]).first()
        finish = prices.filter(price=max_pair[1]).first()

        return JsonResponse({'start': start.month.name if start else None, 'finish': finish.month.name if finish else None}, safe=False)

    def calculate_max_difference(self, prices):
        max_diff = 0
        min_value = prices[0]
        max_pair = (prices[0], prices[0])

        for price in prices:
            if price < min_value:
                min_value = price
            current_diff = price - min_value
            if current_diff > max_diff:
                max_diff = current_diff
                max_pair = (min_value, price)

        return max_diff, min_value, max_pair
