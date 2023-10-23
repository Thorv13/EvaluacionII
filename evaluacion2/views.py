from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'templatesevaluacion2/index1.html')

def chile(request):
    data={
        "titulo":"Chile",
        'imagen1':'/static/imagenes/logo-chile.jpg',
        'dato1':"Es el más largo del mundo con 4.329 kilómetros de longitud, los cuales equivalen a una décima parte de la circunferencia de La Tierra. Pero, su parte más angosta es de 90 kilómetros entre Punta Amolanas y Paso de la Casa Piedra, cerca de Illapel, región de Coquimbo.",
        'dato2':"Los paisajes del Parque Nacional Torres del Paine, en la región de Magallanes, fueron destacados el 2013 entre 300 lugares.",
        'dato3':"Es el Desierto de Atacama con una superficie de 105.000 kilómetros.",
        'dato4':"Se conocen más de 3 mil especies y ninguna es venenosa.",
    }
    return render(request,'templatesevaluacion2/index1.html',data)

def argentina(request):
    data={
        "titulo":"Argentina",
        'imagen2':'/static/imagenes/logo-argentina.jpg',
        'dato1':"Buenos Aires, la bulliciosa capital de Argentina, ostenta el título de tener la calle más ancha del mundo,Esta colosal avenida tiene la asombrosa anchura de 459 pies y 16 carriles de circulación",      
        'dato2':"Argentina es uno de los principales exportadores de carne de vacuno de calidad y goza de gran prestigio internacional. Sus filetes están considerados como unos de los mejores del mundo.", 
        'dato3':"La Laguna del Carbón es un lago salado de origen glaciar situado en la región patagónica de Argentina. Está considerado uno de los lagos más prístinos del mundo debido a su remota ubicación y a la falta de desarrollo humano a su alrededor.",
        'dato4':"El glaciar Perito Moreno es una maravilla natural que atrae a visitantes de todo el mundo a Argentina. El glaciar es único, ya que es uno de los únicos glaciares del mundo que sigue creciendo mientras la mayoría disminuye.",
    }
    return render(request,'templatesevaluacion2/index1.html',data)

def brazil(request):
    data={
        "titulo":"Brazil",
        'imagen3':'/static/imagenes/logo-brazil.jpg',
        'dato1':" El rio Amazonas es el segundo más largo del mundo y el más grande del mundo por volumen",      
        'dato2':" En Brasil viven tribus que aún no han tenido contacto con la vida moderna. En 2007 se contaron hasta 67 tribus que no habían tenido contacto con la vida moderna.", 
        'dato3':" Brasil tiene un tercio de las selvas tropicales del planeta Y por eso también tiene el mayor número de plantas y animales del mundo. Además es el país con mayor número de parques naturales de América.",
        'dato4':"Brasil ha ganado la Copa del Mundo cinco veces. Brasil tiene una gran afición al futbol. Además, su selección de futbol es la única del mundo que ha asistido a todos los mundiales. Su jugador de futbol más famoso es Pelé.",
    }
    return render(request,'templatesevaluacion2/index1.html',data)