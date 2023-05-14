import matplotlib.pyplot as plot

nameChart = 'Chart'
namePie = 'Pie'

def generateBarChart(labels,values):
    fig, axes = plot.subplots()
    axes.bar(labels,values)
    plot.xticks(rotation=90)
    plot.savefig(f'./imgs/{nameChart}IMG.png')

def generatePieChart(Labels,values):
    fig, axes = plot.subplots()
    axes.pie(values,labels=Labels)
    axes.axis('equal')
    plot.xticks(rotation=90)
    plot.savefig(f'./imgs/{namePie}IMGGGGGG.png')
    
    
if __name__ == '__main__':
    generateBarChart()