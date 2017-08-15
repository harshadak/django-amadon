from django.shortcuts import render, HttpResponse, redirect

# the index function is called when root is visited
def index(request):
    return render(request, "amadon/index.html")

def buy(request):
    if request.method == "POST":
        prod_id = int(request.POST['product_id'])
        quant = int(request.POST['quantity'])
        
        if prod_id == 1:
            prod_price = 19.99
        if prod_id == 2:
            prod_price = 29.99
        if prod_id == 3:
            prod_price = 4.99
        if prod_id == 4:
            prod_price = 49.99

        order_price = prod_price * quant

        request.session['order_price'] = order_price

        if "count" in request.session:
            request.session['count'] += quant
            request.session['total'] += order_price
        else:
            request.session['count'] = quant
            request.session['total'] = order_price

        return redirect("/amadon/checkout")
    else:
        return redirect("/")
def checkout(request):
    return render(request, "amadon/thanks.html")

def reset(request):
    request.session.clear()
    return redirect("/")