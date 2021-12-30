def make_plot(base , type):
    import pandas as pd
    import matplotlib.pyplot as plt
    from pandas.io import gbq
    if type == 'Excel': 
        db = pd.read_excel(base)
        db['amount'].plot.area(color ='#44AA99', figsize=(9, 6))
        plt.savefig("herbaly/static/PYPLOT/plot.png" , transparent=True)
        plt.figure()
    elif type == 'Query':
        dp = str(base)
        dp = gbq.read_gbq(dp , project_id='herbalites')
        dp['amount'].plot.area(color ='#44AA99', figsize=(9, 6))
        plt.savefig("herbaly/static/PYPLOT/plot.png" , transparent=True)
        plt.figure()

def make_pie(base , type):
    import pandas as ps
    import matplotlib.pyplot as plot
    from pandas.io import gbq
    if type == 'Excel':
        db = ps.read_excel(base)
        db['currency_iso_code'].value_counts().plot.pie(figsize=(5, 5))
        plot.ylabel('')
        plot.savefig('herbaly/static/PIEPLOT/pie.png', transparent=True)
        plot.figure()
    elif type == 'Query':
        dp = str(base)
        dp = gbq.read_gbq(dp , project_id='herbalites')
        dp['currency_iso_code'].value_counts().plot.pie(figsize=(5, 5))
        plot.ylabel('')
        plot.savefig('herbaly/static/PIEPLOT/pie.png', transparent=True)
        plot.figure()