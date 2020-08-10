from django.shortcuts import render, redirect
from .models import newCatagory, newProducts
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError


nC = newCatagory.objects.all()
p = newProducts.objects.all()
myCart = {}
# Create your views here.
def index(request):
	return render(request, 'home/index.html')
def contact(request):
	return render(request, 'home/pages/contact.html')
def checkout(request):
	return render(request, 'home/pages/checkout.html')

def cart(request):
	total = 0
	myCart = request.session.get('shopcart')
	for item in myCart.values():
		total += item['price']*item['slg']
	return render(request, 'home/pages/cart.html', {'myCart': myCart, 'total': total})


def products(request, id):
	productbyID= newProducts.objects.get(id =id)
	nC = newCatagory.objects.get(id=productbyID.sub_cat_id.id)
	otherProducts = newProducts.objects.filter(sub_cat_id =nC.id)
	return render(request, 'home/pages/products.html', {'productbyID':productbyID, 'listpro': otherProducts})

def probyCat(request, id):
	pbC = newProducts.objects.filter(sub_cat_id=id)
	return render(request, 'home/pages/probycatagory.html', {'nC':nC, 'p':p, 'pbC':pbC})

def catagory(request):
	return render(request, 'home/pages/catagory.html', {'nC':nC, 'p':p})



def insertCart(request, id):
	product = newProducts.objects.get(id=id)

	if request.session.get('shopcart') is None:
		itemCart = {
			'id':id,
			'name': product.pro_name,
			'price': product.pro_price,
			'image': str(product.pro_image),
			'slg': 1
		}
		myCart[id] = itemCart
		request.session['shopcart'] = myCart
	else:		
		if id in myCart.keys():
			itemCart = {
				'id':id,
				'name': product.pro_name,
				'price': product.pro_price,
				'image': str(product.pro_image),
				'slg': int(myCart[id]['slg'])+1
			}
			myCart[id] = itemCart
			request.session['shopcart'] = myCart
		else:
			itemCart = {
				'id':id,
				'name': product.pro_name,
				'price': product.pro_price,
				'image': str(product.pro_image),
				'slg': 1
			}
			myCart[id] = itemCart
			request.session['shopcart'] = myCart

	return redirect('home:catagory')


def deleteCart(request, id):
	myCart = request.session.get('shopcart')

	myCart.pop(str(id), None)


	request.session['shopcart'] = myCart
	return redirect('home:cart')

def updateCart(request):
	slg = request.POST.get("slg", "Guest (or whatever)")

	# lấy id sp, số lượng update rồi ghi đè vào giỏ hàng đang có với id và slgx mới
	return render(request, 'home/check.html', {'myCart': slg})

