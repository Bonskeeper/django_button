from datetime import datetime
from django.shortcuts import render, redirect
from coingate.client import CoinGateClient, CoinGateOrder
from djnago_button.settings import APP_ID, API_KEY, API_SECRET
from .models import ButtonResponse
from .snippets import create_random_order_id


def main_page(request):
    if request.method == 'POST':
        client = CoinGateClient(APP_ID, API_KEY, API_SECRET)
        order_id = create_random_order_id()
        new_order = CoinGateOrder.new(
            order_id,
            10.5,
            "USD",
            "USD",
            callback_url='http://example.com/payments/accept-coingate-callback',
            cancel_url='http://example.com/cart',
            success_url='http://example.com/account/orders')
        try:
            placed_order = client.create_order(new_order)
            status_code = "200 / OK"
            error_or_paymant_url = placed_order.payment_url
            date_created = datetime.now()
        except Exception as error:
            status_code = error
            error_or_paymant_url = error.response['errors']
            date_created = datetime.now()
        new_response = ButtonResponse(status_code=status_code, response_answer=error_or_paymant_url,
                                      response_date=date_created)
        new_response.save()
        return redirect('main')

    responses = ButtonResponse.objects.order_by('-response_date')
    return render(request, 'order_button/main.html', context={'responses': responses})
