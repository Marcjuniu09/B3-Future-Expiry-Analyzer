import pandas as pd
import expiracao_de_contratos_B3 as exp

df = pd.read_excel('symbol.xlsx')
df = pd.read_excel('symbol.xlsx', sheet_name='Sheet1', header=0, index_col=0)

expiration_functions = {'WDO': exp.DOL_WDO_DI1,
                        'DOL': exp.DOL_WDO_DI1,
                        'DI1': exp.DOL_WDO_DI1,
                        'WIN': exp.expiration_WIN,
                        'IND': exp.expiration_IND,
                        'BGI': exp.expiration_BGI_ETN,
                        'ETN': exp.expiration_BGI_ETN,
                        'SFI': exp.expiration_SFI,
                        'CCM': exp.expiration_CCM,
                        'ICF': exp.expiration_ICF}

for index, row in df.iterrows():
    prefix = index[:3]
    if prefix in expiration_functions:
        df.at[index, 'expiration'] = expiration_functions[prefix](index)
