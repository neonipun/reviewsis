import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def show_visuals(rdf):
    #Pie Chart
    sdf = rdf['Sentiment'].value_counts()
    s = sum(sdf.tolist())

    # The slices will be ordered and plotted counter-clockwise.
    labels = sdf.index.tolist()
    fracs = [x / s for x in sdf.tolist()]
    explode=(0.1, 0.1, 0.1)

    fig1, ax1 = plt.subplots()
    ax1.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=30)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Sentiments', bbox={'facecolor':'0.8', 'pad':5})
    plt.show()
