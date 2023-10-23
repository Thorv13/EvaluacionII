from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'templatesProductos/index.html')

def chile(request):
    data={
        "titulo":"Chile",
        'imagen1':'/static/imagenes/logo-foto.jpg',
        'dato1':"Es el más largo del mundo con 4.329 kilómetros de longitud, los cuales equivalen a una décima parte de la circunferencia de La Tierra. Pero, su parte más angosta es de 90 kilómetros entre Punta Amolanas y Paso de la Casa Piedra, cerca de Illapel, región de Coquimbo.",
        'dato2':"Los paisajes del Parque Nacional Torres del Paine, en la región de Magallanes, fueron destacados el 2013 entre 300 lugares.",
        'dato3':"Es el Desierto de Atacama con una superficie de 105.000 kilómetros.",
        'dato4':"Se conocen más de 3 mil especies y ninguna es venenosa.",
    }
    return render(request,'templatesProductos/productos.html',data)

def argentina(request):
    data={
        "titulo":"Argentina",
        'imagen2':'/static/imagenes/logo-foto.jpg',
        'dato1':"Buenos Aires, la bulliciosa capital de Argentina, ostenta el título de tener la calle más ancha del mundo,Esta colosal avenida tiene la asombrosa anchura de 459 pies y 16 carriles de circulación",      
        'dato2':"Argentina es uno de los principales exportadores de carne de vacuno de calidad y goza de gran prestigio internacional. Sus filetes están considerados como unos de los mejores del mundo.", 
        'dato3':"",
        'dato4':"",
    }
    return render(request,'templatesProductos/productos.html',data)

def brazil(request):
    data={
        "titulo":"Chile",
        'imagen3':'/static/imagenes/logo-foto.jpg',
        'dato1':"",      
        'dato2':"", 
        'dato3':"",
        'dato4':"",
    }
    return render(request,'templatesProductos/productos.html',data)