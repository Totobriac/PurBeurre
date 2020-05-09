from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product, SavedProduct
from .management.commands.populate_db import strip_accents
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import re
from django.shortcuts import redirect

# Create your views here.
def index(request):
    template = loader.get_template('finder/main_page.html')
    return HttpResponse(template.render(request=request))

def mentions(request):
    template = loader.get_template('finder/mentions.html')
    return HttpResponse(template.render(request=request))


def search(request):
    query = request.GET.get('query')
    query_lower = query.lower()
    list_name = re.split("[- ’? ; , ' . : ' ' " " ]",query_lower)    
    stripped_query = [strip_accents(x) for x in list_name]      
    stopwords = ['le', 'la', 'les', 'en', 'a', 'au','aux', 'd', 'des', 'et', 'de']
    clean_query =[word for word in stripped_query if word not in stopwords]
    print(clean_query)

    match_list = []
    for x in Product.objects.all():
        match = 0        
        for y in clean_query:
            if y in x.name or y in x.brand:
                match += 1
                if match == len(clean_query):
                    match_list.append(x.id)                
            else:
                pass
    

    if not query:
        products_list= Product.objects.all()        
    else:        
        products_list = Product.objects.filter(id__in=match_list)
    
    title = "Choissisez le produit qui correspond à votre demande: " 

    paginator = Paginator(products_list, 9)
    page = request.GET.get('page',1)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:        
        products = paginator.page(1)
    except EmptyPage:        
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'title': title,
        'paginate': True,
        'query' : query
    }
    return render(request, 'finder/search.html', context)



def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'finder/detail.html', {'product': product})

def substitute(request, product_id):
    product = Product.objects.get(pk=product_id)    
    product_categories = eval(product.categories)   
    match_list=[]    

    for x in Product.objects.all():
        match = 0         
        for y in product_categories[0:4]:
            print(y)
            if y not in eval(x.categories):
                break                       
            elif y in eval(x.categories):                              
                match += 1
                if match == 4:                    
                    match_list.append(x.id)                               
               
    substitute_product = Product.objects.filter(id__in=match_list).order_by('nutrition_grade')

    paginator = Paginator(substitute_product, 9)
    page = request.GET.get('page',1)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:        
        products = paginator.page(1)
    except EmptyPage:        
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,  
        'product': product,       
    }

    return render(request, 'finder/substitute.html', context)

def save(request, product_id, sub_product_id):
    sub_product = Product.objects.get(pk=sub_product_id)
    original_product = Product.objects.get(pk=product_id)
    user = request.user
    previous_page = request.META['HTTP_REFERER']
    p = SavedProduct(username= user, sub_product=sub_product, original_product = original_product)
    p.save()

    response = redirect(previous_page)
    return response
    