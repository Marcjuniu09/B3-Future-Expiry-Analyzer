import pandas as pd
import expiracao_de_contratos_B3 as exp

df = pd.read_excel('symbol.xlsx')
df = pd.read_excel('symbol.xlsx', sheet_name='Sheet1', header=0, index_col=0)

for i, row in df.iterrows():
    if i[:3] == 'WDO':
        df.at[i, 'expiration'] = exp.DOL_WDO_DI1(i)
    elif i[:3] == 'DOL':
        df.at[i, 'expiration'] = exp.DOL_WDO_DI1(i)
    elif i[:3] == 'DI1':
        df.at[i, 'expiration'] = exp.DOL_WDO_DI1(i)
    elif i[:3] == 'WIN':
        df.at[i, 'expiration'] = exp.expiration_WIN(i)
    elif i[:3] == 'IND':
        df.at[i, 'expiration'] = exp.expiration_IND(i)
    elif i[:3] == 'BGI':
        df.at[i, 'expiration'] = exp.expiration_BGI_ETN(i)
    elif i[:3] == 'ETN':
        df.at[i, 'expiration'] = exp.expiration_BGI_ETN(i)
    elif i[:3] == 'SFI':
        df.at[i, 'expiration'] = exp.expiration_SFI(i)
    elif i[:3] == 'CCM':
        df.at[i, 'expiration'] = exp.expiration_CCM(i)
    elif i[:3] == 'ICF':
        df.at[i, 'expiration'] = exp.expiration_ICF(i)
