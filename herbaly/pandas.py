def request_data_base(base , type):
    data_base = {}
    import pandas as pd
    from pandas.io import gbq
    if type == 'Excel':
        db = pd.read_excel(base)
        data_base['amount'] = format(sum(db['amount']),".2f")
        data_base['client'] = db.shape[0]
        data_base['herblyUSD'] = int(db.loc[db['merchant_account_id'] == 'herbalyUSD' , 'merchant_account_id'].value_counts())
        data_base['herblyCAD'] = int(db.loc[db['merchant_account_id'] == 'herbalyCAD' , 'merchant_account_id'].value_counts())
        return data_base
    elif type == 'Query':
        dp = str(base)
        dp = gbq.read_gbq(dp , project_id='herbalites')
        data_base['amount'] = format(sum(dp['amount']),".2f")
        data_base['client'] = dp.shape[0]
        data_base['herblyUSD'] = int(dp.loc[dp['merchant_account_id'] == 'herbalyUSD' , 'merchant_account_id'].value_counts())
        data_base['herblyCAD'] = int(dp.loc[dp['merchant_account_id'] == 'herbalyCAD' , 'merchant_account_id'].value_counts())
        return data_base

