import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy
import matplotlib.pyplot as plt
import matplotlib
from openpyxl import load_workbook
from openpyxl import Workbook
import matplotlib.pyplot as plt
import numpy as np
from math import pi
import pandas as pd
from matplotlib import rc
import plotly.graph_objects as go
from matplotlib import pyplot as plt
import plotly.express as px
import pandas as pd


array_1 = [5,5,5,5,5.2]
array_2 = [7,7,7,7,7.2]
array_3 = [9,9,9,9,9.2]

dimension=5
num_persone=5

def gaussian(array_1,array_2,array_3,dimension):
    i=0
    average_1=0
    for i in range(0,dimension,1):
        average_1=array_1[i]+average_1

    average_1=average_1/dimension
    standard_deviation_1=numpy.std(array_1)


    average_2=0
    for i in range(0,dimension,1):
        average_2=array_2[i]+average_2

    average_2=average_2/dimension
    standard_deviation_2=numpy.std(array_2)

    average_3=0
    for i in range(0,dimension,1):
        average_3=array_3[i]+average_3

    average_3=average_3/dimension
    standard_deviation_3=numpy.std(array_3)
   

    x_all = np.arange(0,7*average_1 , average_1/1000)#this function is used to define the domain of the 
    #function, the first value indicates the starting point, the second the final point, 
    #the third the definition of the approximation
    y1 = norm.pdf(x_all,average_1,standard_deviation_1)
    y2 = norm.pdf(x_all,average_2,standard_deviation_2)
    y3 = norm.pdf(x_all,average_3,standard_deviation_3)  

    # build the plot
    fig, ax = plt.subplots(figsize=(9,6))
    plt.style.use('fivethirtyeight')
    ax.plot(x_all,y1)
    ax.plot(x_all,y2)
    ax.plot(x_all,y3)


    ax.fill_between(x_all,y1,0, alpha=0.3, label ='first array') 
    ax.fill_between(x_all,y2,0, alpha=0.3, label ='second array')
    ax.fill_between(x_all,y3,0, alpha=0.3, label ='third array')

    plt.legend()

    ax.set_xlim([average_2-average_2/1.3,average_2+average_2/2])#it represents the x-axis range shown in the image
    ax.set_yticklabels([])
 
    plt.savefig('normal_curve.png', dpi=7, bbox_inches='tight')
    plt.show()


gaussian(array_1,array_2,array_3,dimension)
