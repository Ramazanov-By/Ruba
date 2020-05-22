from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ContactInfo, Banner, Brand, About
from cart.forms import CartAddProductForm
from django.db.models import Q


def home(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    brands = Brand.objects.all()[:3]
    banners = Banner.objects.all()
    abouts = About.objects.all()

    products = Product.objects.filter(available=True)
    new = Product.objects.filter(new=True).order_by('-created')[:4]
    sale = Product.objects.filter(sale=True).order_by('-created')[:4]

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/index.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'new': new,
                   'sale': sale,
                   'banners': banners,
                   'abouts': abouts,
                   'brands':brands})


def contacts_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    contacts = ContactInfo.objects.get(pk=1)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

    return render(request,
                  'shop/contacts.html',
                  {'category': category,
                   'categories': categories,
                   'contacts': contacts})


def about(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    about = About.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

    return render(request,
                  'shop/about.html',
                  {'category': category,
                   'categories': categories,
                   'about': about})


def brand(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    brands = Brand.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

    return render(request,
                  'shop/brand.html',
                  {'category': category,
                   'categories': categories,
                   'brands': brands})


def product_list(request, category_slug=None):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    else:
        products = Product.objects.filter(available=True)
    category = None
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_listNew(request, category_slug=None):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    else:
        products = Product.objects.filter(available=True, new=True)
    category = None
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/listNew.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_listSale(request, category_slug=None):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    else:
        products = Product.objects.filter(available=True, sale=True)
    category = None
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/listSale.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    category = None
    categories = Category.objects.all()

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'category': category,
                   'categories': categories
                   })


