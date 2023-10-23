from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'templatesProductos/index.html')

def electronica(request):
    data={
        "titulo":"Electrónica",
        'producto1':"MAC",
        'imagen1':'/static/imagenes/logo-foto.jpg',
        'producto2':"Celular",
        'imagen2':'/static/imagenes/logo-foto.jpg',
        'producto3':"PlayStation",
        'imagen3':'/static/imagenes/logo-foto.jpg'
    }
    return render(request,'templatesProductos/productos.html',data)

def ropa(request):
    data={
        "titulo":"Ropa",
        'producto1':"Polera",
        'imagen1':'/static/imagenes/logo-foto.jpg',
        'producto2':"Chaqueta",
        'imagen2':'/static/imagenes/logo-foto.jpg',
        'producto3':"Zapatilla",
        'imagen3':'/static/imagenes/logo-foto.jpg'
    }
    return render(request,'templatesProductos/productos.html',data)

def juguetes(request):
    data={
        "titulo":"Juguetes",
        'producto1':"Pelota",
        'imagen1':'/static/imagenes/logo-foto.jpg',
        'producto2':"Figuras de acción",
        'imagen2':'/static/imagenes/logo-foto.jpg',
        'producto3':"Juegos de mesa",
        'imagen3':'/static/imagenes/logo-foto.jpg',
        
    }
    return render(request,'templatesProductos/productos.html',data)