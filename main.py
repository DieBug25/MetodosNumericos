from flask import Flask, render_template, url_for, request,redirect
import math
import numpy as np
import pygal


app = Flask(__name__)

app.secret_key = 'mysecretkey'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/regresion_tam')
def reg_tam():
    return render_template('regresion_elegir_tam.html')

@app.route('/modelo_tam')
def mod_tam():
    return render_template('modelo_tam.html')

@app.route('/ecuacion_tam')
def ecu_tam():
    return render_template('ecuacion_tam.html')

@app.route('/razon_tam')
def razon_tam():
    return render_template('razon_tam.html')

@app.route('/polinomio2_tam')
def pol2_tam():
    return render_template('pol2_tam.html')

@app.route('/polinomio3_tam')
def pol3_tam():
    return render_template('pol3_tam.html')

@app.route('/table_regresion', methods = ['POST'])
def table():
    size = request.form['size']
    val = int(size)
    Lista_tabla = []
    for x in range(0,val):
        Lista_tabla.append(x)
    return render_template('table_regresion.html', num = Lista_tabla, val = val)

@app.route('/table_modelo', methods = ['POST'])
def table_mod():
    size = request.form['size']
    val = int(size)
    Lista_tabla = []
    for x in range(0,val):
        Lista_tabla.append(x)
    return render_template('table_modelo.html', num = Lista_tabla, val = val)

@app.route('/table_ecuacion', methods = ['POST'])
def table_ec():
    size = request.form['size']
    val = int(size)
    Lista_tabla = []
    for x in range(0,val):
        Lista_tabla.append(x)
    return render_template('table_ecuacion.html', num = Lista_tabla, val = val)

@app.route('/table_razon', methods = ['POST'])
def table_razon():
    size = request.form['size']
    val = int(size)
    Lista_tabla = []
    for x in range(0,val):
        Lista_tabla.append(x)
    return render_template('table_razon.html', num = Lista_tabla, val = val)

@app.route('/table_pol2', methods = ['POST'])
def table_pol2():
    size = request.form['size']
    val = int(size)
    Lista_tabla = []
    for x in range(0,val):
        Lista_tabla.append(x)
    return render_template('table_pol2.html', num = Lista_tabla, val = val)

@app.route('/table_pol3', methods = ['POST'])
def table_pol3():
    size = request.form['size']
    val = int(size)
    Lista_tabla = []
    for x in range(0,val):
        Lista_tabla.append(x)
    return render_template('table_pol3.html', num = Lista_tabla, val = val)



 

@app.route('/resolver_regresion/<val>', methods = ['POST'])
def resolver(val):
  x=[]
  y=[]
  valor = int(val)
  prueba=[]
  for k in range(0,valor):
     x.append(float(request.form['x_'+str(k)]))
     y.append(float(request.form['y_'+str(k)]))
  for z in range(0,valor):
     prueba.append((x[z],y[z]))

  sumax=0
  sumay=0
  sumaxy=0
  sumac=0
  promy=0
  promx=0
  a0=0
  a1=0
  x2=0
  sumst=0
  sumsr=0
  sy=0
  syx=0
  r=0
  for i in range(0,valor):
      sumac=sumac+1
      sumax +=x[i]
      sumay += y[i]
      sumaxy += x[i]*y[i]
      x2 += x[i]*x[i]

  promx = sumax/sumac
  promy = sumay/sumac
  a1=(sumac*sumaxy-(sumax*sumay))/(sumac*x2-(sumax*sumax))
  a0 = promy-(a1*promx)


  for j in range(0,valor):
      sumst += (y[j]-promy)*(y[j]-promy)
      sumsr += (y[j]-a0-(a1*x[j]))*(y[j]-a0-(a1*x[j]))
  sy = math.sqrt(sumst/(sumac-1))
  syx = math.sqrt(sumsr/(sumac-2))
  r = math.sqrt((sumst-sumsr)/sumst)*100
  desEstandar = "Desviacion estandar = "+str(sy)
  errEstandar = "Error estandar = "+str(syx)
  coeCorrelacion = "Coeficiente de correlacion = "+str(r)+"%"
  funcion = "Y = "+str(a0)+" + "+str(a1)+"X"
     
  try:
     xy_chart = pygal.XY(stroke=False)
     xy_chart.title = 'Dot chart'
     xy_chart.add('Values', prueba)
     graph_data = xy_chart.render_data_uri()
     prueba1=[]
     for z in range(-20,20):
         prueba1.append(a0+(a1*z))
     print(prueba1)
     line_chart = pygal.Line()
     line_chart.title = 'Function graph'
     line_chart.x_labels = map(str, range(-20, 20))
     line_chart.add('Values', prueba1)
     graph_data2 = line_chart.render_data_uri()
     

     return render_template("graphing.html",graph_data = graph_data, graph_data2 = graph_data2,coeCorrelacion=coeCorrelacion,errEstandar=errEstandar,desEstandar=desEstandar, funcion = funcion,listx=x,listy=y)
  except:
        print("Error")
    
@app.route('/resolver_modelo/<val>', methods = ['POST'])
def resolver_modelo(val):
    x = []
    y = []
    logy = []
    valor = int(val)
    prueba=[]
    for z in range(0,valor):
        x.append(float(request.form['x_'+str(z)]))
        y.append(float(request.form['y_'+str(z)]))
    
    for p in range(0,valor):
        logy.append(float(math.log(y[p])))
        prueba.append((x[p], y[p]))
    

    sumax=0
    sumay=0
    sumaxy=0
    sumac=0
    promy=0
    promx=0
    a0=0
    a1=0
    x2 = 0 
    sumst = 0
    sumsr = 0
    sy=0
    syx=0
    r=0
    for i in range(0,valor):
        sumac = sumac+1
        sumax += x[i]
        sumay += logy[i]
        sumaxy +=x[i]*logy[i]
        x2 += x[i]*x[i]
    
    promx = sumax/sumac
    promy = sumay/sumac
    a1 = (sumac*sumaxy-(sumax*sumay))/(sumac*x2-(sumax*sumax))
    a0 = promy-a1*promx
    

    for j in range(0,valor):
        sumst += math.pow((logy[j]-promy),2)
        sumsr += math.pow(logy[j]-a0-(a1*x[j]),2)
    a0 = math.exp(a0)
    sy = math.sqrt(sumst/(sumac-1))
    syx = math.sqrt(sumsr/(sumac-2))
    r = math.sqrt((sumst-sumsr)/(sumst))*100
    desEstandar = "Desviación estándar = "+str(sy)
    errEstandar = "Error estándar = "+str(syx)
    coeCorrelacion = "Coeficiente de correlación = "+str(r)+"%"

    funcion = "Y = "+str(a0)+"e^"+str(a1)+"X"
    try:
     xy_chart = pygal.XY(stroke=False)
     xy_chart.title = 'Dot chart'
     xy_chart.add('Values', prueba)
     graph_data = xy_chart.render_data_uri()
     prueba1=[]
     for z in range(-20,20):
         prueba1.append(a0*(math.exp(a1*z)))
     print(prueba1)
     line_chart = pygal.Line()
     line_chart.title = 'Function graph'
     line_chart.x_labels = map(str, range(-20, 20))
     line_chart.add('Values', prueba1)
     graph_data2 = line_chart.render_data_uri()
     

     return render_template("graphing.html", graph_data = graph_data, graph_data2 = graph_data2,coeCorrelacion=coeCorrelacion,errEstandar=errEstandar,desEstandar=desEstandar, funcion = funcion,listx=x,listy=y)
    except:
      print("Error")


@app.route('/resolver_ecuacion/<val>', methods = ['POST'])
def resolver_ec(val):
    x = []
    y = []
    valor = int(val)
    logy=[]
    logx=[]
    prueba=[]
    for k in range(0,valor):
     x.append(float(request.form['x_'+str(k)]))
     y.append(float(request.form['y_'+str(k)]))
    
    for z in range(0,valor):
        logy.append(float(math.log10(y[z])))
        logx.append(float(math.log10(x[z])))
        prueba.append((x[z], y[z]))

    sumax=0
    sumay=0
    sumaxy=0
    sumac=0
    promy=0
    promx=0
    a0=0
    a1=0
    x2 = 0
    sumst = 0
    sumsr = 0
    sy=0
    syx=0
    r=0
    
    for i in range(0,valor):
        sumac=sumac+1
        sumax +=logx[i]
        sumay += logy[i]
        sumaxy += logx[i]*logy[i]
        x2 += logx[i]*logx[i]
    
    promx = sumax/sumac
    promy = sumay/sumac
    a1 = (sumac*sumaxy-(sumax*sumay))/(sumac*x2-(sumax*sumax))
    a0 = promy-(a1*promx)

    for j in range(0,valor):
        sumst += math.pow((logy[j]-promy),2)
        sumsr += (logy[j]-a0-(a1*logx[j]))*(logy[j]-a0-(a1*logx[j]))
    a0 = math.pow(10,a0)
    sy = math.sqrt(sumst/(sumac-1))
    syx = math.sqrt(sumsr/(sumac-2))
    r = math.sqrt((sumst-sumsr)/(sumst))*100
    desEstandar = "Desviación estándar = "+str(sy)
    errEstandar = "Error estándar = "+str(syx)
    coeCorrelacion = "Coeficiente de correlación = "+str(r)+"%"

    funcion = "Y = "+str(a0)+"x^"+str(a1)
    
    
    try:
     xy_chart = pygal.XY(stroke=False)
     xy_chart.title = 'Dot chart'
     xy_chart.add('Values', prueba)
     graph_data = xy_chart.render_data_uri()
     prueba1=[]
     for z in range(0,20):
         prueba1.append((a0)*(math.pow(z,a1)))
     print(prueba1)
     line_chart = pygal.Line()
     line_chart.title = 'Function graph'
     line_chart.x_labels = map(str, range(-20, 20))
     line_chart.add('Values', prueba1)
     graph_data2 = line_chart.render_data_uri() 
     

     return render_template("graphing.html", graph_data = graph_data, graph_data2 = graph_data2,coeCorrelacion=coeCorrelacion,errEstandar=errEstandar,desEstandar=desEstandar, funcion = funcion,listx=x,listy=y)
    except:
      print("Error")

@app.route('/resolver_razon/<val>', methods=['POST'])
def resolver_razon(val):
    x = []
    y = []
    valor = int(val)
    prueba=[]
    for z in range (0,valor): 
        x.append(float(request.form['x_'+str(z)]))
        y.append(float(request.form['y_'+str(z)]))
       
    for z in range(0,valor):
     prueba.append((x[z],y[z]))
     x[z]=1/x[z]
     y[z]=1/y[z]
    
    sumax=0
    sumay=0
    sumaxy=0
    sumac=0
    promy=0
    promx=0
    a0=0
    a1=0
    x2 = 0
    sumst = 0
    sumsr = 0
    sy=0
    syx=0
    r=0

    for i in range(0,valor):
        sumac=sumac+1
        sumax +=x[i]
        sumay += y[i]
        sumaxy += x[i]*y[i]
        x2 += x[i]*x[i]
    
    promx = sumax/sumac
    promy = sumay/sumac
    a1 = (sumac*sumaxy-(sumax*sumay))/(sumac*x2-(sumax*sumax))
    a0 = promy-(a1*promx)

    for j in range(0,valor):
        sumst += math.pow((y[j]-promy),2)
        sumsr += (y[j]-a0-(a1*x[j]))*(y[j]-a0-(a1*x[j]))
    sy = math.sqrt(sumst/(sumac-1))
    syx = math.sqrt(sumsr/(sumac-2))
    r = math.sqrt((sumst-sumsr)/(sumst))*100
    a0 = 1/a0
    a1 = a1/a0
    
    desEstandar = "Desviación estándar = "+str(sy)
    errEstandar = "Error estándar = "+str(syx)
    coeCorrelacion = "Coeficiente de correlación = "+str(r)+"%"


    funcion = "Y = "+str(a0)+"x/"+str(a1)+"X"
    try:
     xy_chart = pygal.XY(stroke=False)
     xy_chart.title = '%Correlation'
     xy_chart.add('Values', prueba)
     graph_data = xy_chart.render_data_uri()
     prueba1=[]
     for z in range(-20,20):
         prueba1.append(a0*(z/a1*z))
     print(prueba1)
     line_chart = pygal.Line()
     line_chart.title = 'Function graph'
     line_chart.x_labels = map(str, range(-20, 20))
     line_chart.add('Values', prueba1)
     graph_data2 = line_chart.render_data_uri()

     return render_template("graphing.html", graph_data = graph_data, graph_data2 = graph_data2,coeCorrelacion=coeCorrelacion,errEstandar=errEstandar,desEstandar=desEstandar, funcion = funcion,listx=x,listy=y)
    except:
      print("Error")

@app.route('/resolver_pol2/<val>', methods=['POST'])
def resolver_pol2(val):
    x = []
    y = []
    valor = int(val)
    prueba=[]
    for z in range (0,valor): 
        x.append(float(request.form['x_'+str(z)]))
        y.append(float(request.form['y_'+str(z)]))
        prueba.append((x[z],y[z]))
    
    sumax=0
    sumay=0
    sumaxy=0
    sumac=0
    promy=0
    promx=0
    a0=0
    a1=0
    sumx2 = []
    x2 = 0
    x3 = 0
    x4 = 0
    x2y = 0
    sumst = 0
    sumsr = 0
    a2=0
    sy=0
    syx=0
    r=0

    for i in range(0,valor):
        sumac = sumac+1
        sumax += x[i]
        sumay += y[i]
        x2 += math.pow(x[i],2)
        sumx2.append(x[i]*x[i])
        x3 += math.pow(x[i],3)
        x4 += math.pow(x[i],4) 
        sumaxy += x[i]*y[i]
        x2y += (math.pow(x[i],2))*y[i]

    promy = sumay/sumac
    a=np.array([[sumac,sumax,x2],[sumax,x2,x3],[x2,x3,x4]])
    b = np.array([sumay,sumaxy,x2y])
    sol = np.linalg.solve(a,b)
    a0 = sol[0]
    a1 = sol[1]
    a2 = sol[2]
    for j in range(0,valor):
        sumst += math.pow((y[j]-promy),2)
        sumsr += math.pow(y[j]-a0-(a1*x[j])-(a2*sumx2[j]),2)
 
    
    sy = math.sqrt(sumst/(sumac-1))
    syx = math.sqrt(sumsr/(sumac-3))
    r = math.sqrt((sumst-sumsr)/(sumst))*100
    desEstandar = "Desviacion estandar = "+str(sy)
    errEstandar = "Error estandar = "+str(syx)
    coeCorrelacion = "Coeficiente de correlación = "+str(r)+"%"
    funcion = "Y = "+str(a0)+"(+)"+str(a1)+"X(+)"+str(a2)+"x^2"

    try:
     xy_chart = pygal.XY(stroke=False)
     xy_chart.title = 'Dot chart'
     xy_chart.add('Values', prueba)
     graph_data = xy_chart.render_data_uri()
     prueba1=[]
     for z in range(-20,20):
         prueba1.append(a0+a1*z+a2*math.pow(z,2))
     print(prueba1)
     line_chart = pygal.Line()
     line_chart.title = 'Function graph'
     line_chart.x_labels = map(str, range(-20, 20))
     line_chart.add('Values', prueba1)
     graph_data2 = line_chart.render_data_uri()

     return render_template("graphing.html", graph_data = graph_data, graph_data2 = graph_data2,coeCorrelacion=coeCorrelacion,errEstandar=errEstandar,desEstandar=desEstandar, funcion = funcion,listx=x,listy=y)
    except:
        print("Error")

@app.route('/resolver_pol3/<val>', methods=['POST'])
def resolver_pol3(val):
    x = []
    y = []
    valor = int(val)
    prueba=[]
    for z in range (0,valor): 
        x.append(float(request.form['x_'+str(z)]))
        y.append(float(request.form['y_'+str(z)]))
        prueba.append((x[z],y[z]))
    
    sumax=0
    sumay=0
    sumaxy=0
    sumac=0
    promy=0
    promx=0
    a0=0
    a1=0
    sumx2 = []
    sumx3 = []
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    x6 = 0
    x2y = 0
    x3y = 0
    sumst = 0
    sumsr = 0
    a2=0
    a3 = 0
    sy=0
    syx=0
    r=0

    for i in range(0,valor):
        sumac = sumac+1
        sumax += x[i]
        sumay += y[i]
        x2 += math.pow(x[i],2)
        sumx2.append(x[i]*x[i])
        sumx3.append(math.pow(x[i],3))
        x3 += math.pow(x[i],3)
        x4 += math.pow(x[i],4)
        x5 += math.pow(x[i],5)
        x6 += math.pow(x[i],6)
        sumaxy += x[i]*y[i]
        x2y += (math.pow(x[i],2))*y[i]
        x3y += (math.pow(x[i],3))*y[i]

    promy = sumay/sumac
    a=np.array([[sumac,sumax,x2,x3],[sumax,x2,x3,x4],[x2,x3,x4,x5],[x3,x4,x5,x6]])
    b = np.array([sumay,sumaxy,x2y,x3y])
    sol = np.linalg.solve(a,b)
    a0 = sol[0]
    a1 = sol[1]
    a2 = sol[2]
    a3 = sol[3]
    for j in range(0,valor):
        sumst += math.pow((y[j]-promy),2)
        sumsr += math.pow(y[j]-a0-(a1*x[j])-(a2*sumx2[j])-(a3*sumx3[j]),2)
 
    
    sy = math.sqrt(sumst/(sumac-1))
    syx = math.sqrt(sumsr/(sumac-3))
    r = math.sqrt((sumst-sumsr)/(sumst))*100
    desEstandar = "Desviacion estandar = "+str(sy)
    errEstandar = "Error estandar = "+str(syx)
    coeCorrelacion = "Coeficiente de correlación = "+str(r)+"%"
    funcion = "Y = "+str(a0)+"(+)"+str(a1)+"X(+)"+str(a2)+"x^2(+)"+str(a3)+"x^3"

    try:
     xy_chart = pygal.XY(stroke=False)
     xy_chart.title = 'Dot chart'
     xy_chart.add('Values', prueba)
     graph_data = xy_chart.render_data_uri()
     prueba1=[]
     for z in range(-20,20):
         prueba1.append(a0+a1*z+a2*math.pow(z,2)+a3*math.pow(z,3))
     print(prueba1)
     line_chart = pygal.Line()
     line_chart.title = 'Function graph'
     line_chart.x_labels = map(str, range(-20, 20))
     line_chart.add('Values', prueba1)
     graph_data2 = line_chart.render_data_uri()

     return render_template("graphing.html", graph_data = graph_data, graph_data2 = graph_data2,coeCorrelacion=coeCorrelacion,errEstandar=errEstandar,desEstandar=desEstandar, funcion = funcion,listx=x,listy=y)
    except:
        print("Error")


@app.route('/pygalexample/')
def pygalexample():  
  try:
     prueba = []
     funcion1=0.06112912
     funcion2=1.76548907
     for z in range(0,20):
         prueba.append(funcion1*math.pow(z,funcion2))
     print(prueba)
     line_chart = pygal.Line()
     line_chart.title = 'Browser usage evolution (in %)'
     line_chart.x_labels = map(str, range(0, 99))
     line_chart.add('Firefox', prueba)
     graph_data = line_chart.render_data_uri()
     return render_template("graphing.html", graph_data = graph_data)
  except:
        print("Error")

    
	
	

if __name__ == '__main__':
    app.run(debug = True)