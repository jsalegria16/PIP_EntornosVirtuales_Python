import matplotlib.pyplot as plt
def generate_pie_chart():
    labels = ['a','b','c','d']
    values = [100,212,30,50]
    
    fix,axes = plt.subplots()
    axes.pie(values,labels=labels)
    plt.savefig('piegraph.png') # Para gurdar la imagen porque el plt.show() detiene el programa
    plt.close()