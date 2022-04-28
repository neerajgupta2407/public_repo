import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np
labels = 'google', 'bing', 'fb'
mycolors = 'red','green', 'blue'
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
budget_graph_data = {"bing":{"currency":"GBP","monthly_spend":74.39999999999999,"current_overspend":-264.67,"monthly_budget":2543,"daily_budget":84.77,"overspend_last_days_sequence":0,"overspend_days_in_last_5_days":0,"overspend_amount_in_last_5_days":-349.43,"predicted_overspend":-1985,"predicted_overspend_percent":-0.78,"current_spend":[{"date":"2022-04-01","sum_spend":24.31},{"date":"2022-04-02","sum_spend":46.04},{"date":"2022-04-03","sum_spend":72.35},{"date":"2022-04-04","sum_spend":74.39999999999999}],"predicted_spend":[{"date":"2022-04-05","sum_spend":96.4},{"date":"2022-04-06","sum_spend":118.4},{"date":"2022-04-07","sum_spend":140.4},{"date":"2022-04-08","sum_spend":162.4},{"date":"2022-04-09","sum_spend":184.4},{"date":"2022-04-10","sum_spend":206.4},{"date":"2022-04-11","sum_spend":228.4},{"date":"2022-04-12","sum_spend":250.4},{"date":"2022-04-13","sum_spend":272.4},{"date":"2022-04-14","sum_spend":294.4},{"date":"2022-04-15","sum_spend":316.4},{"date":"2022-04-16","sum_spend":338.4},{"date":"2022-04-17","sum_spend":360.4},{"date":"2022-04-18","sum_spend":382.4},{"date":"2022-04-19","sum_spend":404.4},{"date":"2022-04-20","sum_spend":426.4},{"date":"2022-04-21","sum_spend":448.4},{"date":"2022-04-22","sum_spend":470.4},{"date":"2022-04-23","sum_spend":492.4},{"date":"2022-04-24","sum_spend":514.4},{"date":"2022-04-25","sum_spend":536.4},{"date":"2022-04-26","sum_spend":558.4},{"date":"2022-04-27","sum_spend":580.4},{"date":"2022-04-28","sum_spend":602.4},{"date":"2022-04-29","sum_spend":624.4},{"date":"2022-04-30","sum_spend":646.4}],"ideal_spend":[{"date":"2022-04-01","sum_spend":84.77},{"date":"2022-04-02","sum_spend":169.53},{"date":"2022-04-03","sum_spend":254.3},{"date":"2022-04-04","sum_spend":339.07},{"date":"2022-04-05","sum_spend":423.83},{"date":"2022-04-06","sum_spend":508.6},{"date":"2022-04-07","sum_spend":593.37},{"date":"2022-04-08","sum_spend":678.13},{"date":"2022-04-09","sum_spend":762.9},{"date":"2022-04-10","sum_spend":847.67},{"date":"2022-04-11","sum_spend":932.43},{"date":"2022-04-12","sum_spend":1017.2},{"date":"2022-04-13","sum_spend":1101.97},{"date":"2022-04-14","sum_spend":1186.73},{"date":"2022-04-15","sum_spend":1271.5},{"date":"2022-04-16","sum_spend":1356.27},{"date":"2022-04-17","sum_spend":1441.03},{"date":"2022-04-18","sum_spend":1525.8},{"date":"2022-04-19","sum_spend":1610.57},{"date":"2022-04-20","sum_spend":1695.33},{"date":"2022-04-21","sum_spend":1780.1},{"date":"2022-04-22","sum_spend":1864.87},{"date":"2022-04-23","sum_spend":1949.63},{"date":"2022-04-24","sum_spend":2034.4},{"date":"2022-04-25","sum_spend":2119.17},{"date":"2022-04-26","sum_spend":2203.93},{"date":"2022-04-27","sum_spend":2288.7},{"date":"2022-04-28","sum_spend":2373.47},{"date":"2022-04-29","sum_spend":2458.23},{"date":"2022-04-30","sum_spend":2543}]},"google":{"currency":"GBP","monthly_spend":3766.973338,"current_overspend":-2233.03,"monthly_budget":45000,"daily_budget":1500,"overspend_last_days_sequence":0,"overspend_days_in_last_5_days":0,"overspend_amount_in_last_5_days":-3733.03,"predicted_overspend":-16747.7,"predicted_overspend_percent":-0.37,"current_spend":[{"date":"2022-04-01","sum_spend":1046.284971},{"date":"2022-04-02","sum_spend":2315.613248},{"date":"2022-04-03","sum_spend":3691.191841},{"date":"2022-04-04","sum_spend":3766.973338}],"predicted_spend":[{"date":"2022-04-05","sum_spend":4672.97},{"date":"2022-04-06","sum_spend":5578.97},{"date":"2022-04-07","sum_spend":6484.97},{"date":"2022-04-08","sum_spend":7390.97},{"date":"2022-04-09","sum_spend":8296.97},{"date":"2022-04-10","sum_spend":9202.97},{"date":"2022-04-11","sum_spend":10108.97},{"date":"2022-04-12","sum_spend":11014.97},{"date":"2022-04-13","sum_spend":11920.97},{"date":"2022-04-14","sum_spend":12826.97},{"date":"2022-04-15","sum_spend":13732.97},{"date":"2022-04-16","sum_spend":14638.97},{"date":"2022-04-17","sum_spend":15544.97},{"date":"2022-04-18","sum_spend":16450.97},{"date":"2022-04-19","sum_spend":17356.97},{"date":"2022-04-20","sum_spend":18262.97},{"date":"2022-04-21","sum_spend":19168.97},{"date":"2022-04-22","sum_spend":20074.97},{"date":"2022-04-23","sum_spend":20980.97},{"date":"2022-04-24","sum_spend":21886.97},{"date":"2022-04-25","sum_spend":22792.97},{"date":"2022-04-26","sum_spend":23698.97},{"date":"2022-04-27","sum_spend":24604.97},{"date":"2022-04-28","sum_spend":25510.97},{"date":"2022-04-29","sum_spend":26416.97},{"date":"2022-04-30","sum_spend":27322.97}],"ideal_spend":[{"date":"2022-04-01","sum_spend":1500},{"date":"2022-04-02","sum_spend":3000},{"date":"2022-04-03","sum_spend":4500},{"date":"2022-04-04","sum_spend":6000},{"date":"2022-04-05","sum_spend":7500},{"date":"2022-04-06","sum_spend":9000},{"date":"2022-04-07","sum_spend":10500},{"date":"2022-04-08","sum_spend":12000},{"date":"2022-04-09","sum_spend":13500},{"date":"2022-04-10","sum_spend":15000},{"date":"2022-04-11","sum_spend":16500},{"date":"2022-04-12","sum_spend":18000},{"date":"2022-04-13","sum_spend":19500},{"date":"2022-04-14","sum_spend":21000},{"date":"2022-04-15","sum_spend":22500},{"date":"2022-04-16","sum_spend":24000},{"date":"2022-04-17","sum_spend":25500},{"date":"2022-04-18","sum_spend":27000},{"date":"2022-04-19","sum_spend":28500},{"date":"2022-04-20","sum_spend":30000},{"date":"2022-04-21","sum_spend":31500},{"date":"2022-04-22","sum_spend":33000},{"date":"2022-04-23","sum_spend":34500},{"date":"2022-04-24","sum_spend":36000},{"date":"2022-04-25","sum_spend":37500},{"date":"2022-04-26","sum_spend":39000},{"date":"2022-04-27","sum_spend":40500},{"date":"2022-04-28","sum_spend":42000},{"date":"2022-04-29","sum_spend":43500},{"date":"2022-04-30","sum_spend":45000}]}}
def gen_pie_chart():
    sizes = [15, 30, 45]
    explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            colors=mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # draw circle
    centre_circle = plt.Circle((0, 0), 0.40, fc='white')
    fig = plt.gcf()

    # Adding Circle in Pie chart
    fig.gca().add_artist(centre_circle)
    plt.savefig('images/pie.png')
    plt.show()

def gen_hor_graph():
    plt.barh(labels, [4.27,1.84,1.44], height=0.2, color = mycolors)
    plt.rcParams['axes.facecolor'] = 'none' # Set BG color as None.
    plt.savefig('images/CPC_CPA.png')
    plt.show()

def gen_budget_graph():
    bing_data = budget_graph_data['bing']



    # Set up the axes and figure
    fig, ax = plt.subplots()

    plt.plot( 'date', 'sum_spend', data=pd.DataFrame(bing_data['current_spend'], columns=['date', 'sum_spend']), marker='o', markerfacecolor='red', markersize=8, color='skyblue', linewidth=4,label="Actual Spend")
    plt.plot( 'date', 'sum_spend', data=pd.DataFrame(bing_data['predicted_spend'], columns=['date', 'sum_spend']), marker='o', markerfacecolor='blue', markersize=8, color='skyblue', linewidth=4,label="Predicted Spend")
    plt.plot( 'date', 'sum_spend', data=pd.DataFrame(bing_data['ideal_spend'], columns=['date', 'sum_spend']), marker='o', markerfacecolor='black', markersize=8, color='skyblue', linewidth=4, label="Ideal Spend")
    # ax.xaxis_date()
    # fig.autofmt_xdate()
    # show legend
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.savefig('images/budget_graph.png')
    plt.show()


