import pandas as pd

columns_eff = ['N°','college','promotion','inscrits M','inscrits F','inscrits T',
           'ayant composé M','ayant composé F','ayant composé T',
           'sans notes M','sans notes F','sans notes T',
           'forte moyenne M','forte moyenne F', 'faible moyenne M','faible moyenne F',
           'inf_6.5_m','inf_6.5_f','inf_6.5_t','6.5_7.5_m','6.5_7.5_f','6.5_7.5_t',
           '[7.5 9[_M','[7.5 9[_F','[7.5 9[_T','[9 10[_M','[9 10[_F','[9 10[_T','10_11_m','10_11_f','10_11_t',
           '11_12_m','11_12_f','11_12_t','12_14_m','12_14_f','12_14_t','14_16_m','14_16_f','14_16_t',
           '[sup 16[_M','[sup 16[_F','[sup 16[_T']

columns_prcent = ['N°','college','promotion', 'ayant composé M','ayant composé F','ayant composé T',
                  'sans notes M','sans notes F','sans notes T',
           'inf_6.5_m','inf_6.5_f','inf_6.5_t','6.5_7.5_m','6.5_7.5_f','6.5_7.5_t',
           '[7.5 9[_M','[7.5 9[_F','[7.5 9[_T','[9 10[_M','[9 10[_F','[9 10[_T','10_11_m','10_11_f','10_11_t',
           '11_12_m','11_12_f','11_12_t','12_14_m','12_14_f','12_14_t','14_16_m','14_16_f','14_16_t',
           '[sup 16[_M','[sup 16[_F','[sup 16[_T']


def load_data_eff():
    return pd.read_csv('C:/Users/ok/school_results/school_results_git/data/data_eff.csv')

def load_data_prcent():
    return pd.read_csv('C:/Users/ok/school_results/school_results_git/data/data_prcent.csv')




def processing(df):
    if len(df.columns) == 43:
        df.columns = columns_eff
        df['N°'] = df['N°'] + 1
        df['[inf 7.5[_M'] = df['inf_6.5_m'] + df['6.5_7.5_m']
        df['[inf 7.5[_F'] = df['inf_6.5_f'] + df['6.5_7.5_f']
        df['[inf 7.5[_T'] = df['inf_6.5_t'] + df['6.5_7.5_t']

        df['[10_12[_M'] = df['10_11_m'] + df['11_12_m']
        df['[10_12[_F'] = df['10_11_f'] + df['11_12_f']
        df['[10_12[_T'] = df['10_11_t'] + df['11_12_t']

        df['[sup 14[_M'] = df['[sup 16[_M'] + df['14_16_m']
        df['[sup 14[_F'] = df['[sup 16[_F'] + df['14_16_f']
        df['[sup 14[_T'] = df['[sup 16[_T'] + df['14_16_t']

        df['[sup 12[_M'] = df['[sup 14[_M'] + df['12_14_m']
        df['[sup 12[_F'] = df['[sup 14[_F'] + df['12_14_f']
        df['[sup 12[_T'] = df['[sup 14[_T'] + df['12_14_t']

        df['[sup 10[_M'] = df['[sup 12[_M'] + df['[10_12[_M']
        df['[sup 10[_F'] = df['[sup 12[_F'] + df['[10_12[_F']
        df['[sup 10[_T'] = df['[sup 12[_T'] + df['[10_12[_T']

        return df[['N°','college','promotion','inscrits M','inscrits F','inscrits T',
           'ayant composé M','ayant composé F','ayant composé T',
           'sans notes M','sans notes F','sans notes T',
           'forte moyenne M','forte moyenne F', 'faible moyenne M','faible moyenne F',
           '[inf 7.5[_M','[inf 7.5[_F','[inf 7.5[_T','[7.5 9[_M','[7.5 9[_F','[7.5 9[_T',
           '[9 10[_M','[9 10[_F','[9 10[_T','[10_12[_M','[10_12[_F','[10_12[_T',
           '[sup 10[_M','[sup 10[_F','[sup 10[_T','[sup 12[_M','[sup 12[_F','[sup 12[_T',
            '[sup 14[_M','[sup 14[_F','[sup 14[_T','[sup 16[_M','[sup 16[_F','[sup 16[_T']]

    elif len(df.columns) == 36:
        df.columns = columns_prcent
        df['N°'] = df['N°'] + 1
        df['[inf 7.5[_M'] = df['inf_6.5_m'] + df['6.5_7.5_m']
        df['[inf 7.5[_F'] = df['inf_6.5_f'] + df['6.5_7.5_f']
        df['[inf 7.5[_T'] = df['inf_6.5_t'] + df['6.5_7.5_t']

        df['[10_12[_M'] = df['10_11_m'] + df['11_12_m']
        df['[10_12[_F'] = df['10_11_f'] + df['11_12_f']
        df['[10_12[_T'] = df['10_11_t'] + df['11_12_t']

        df['[sup 14[_M'] = df['[sup 16[_M'] + df['14_16_m']
        df['[sup 14[_F'] = df['[sup 16[_F'] + df['14_16_f']
        df['[sup 14[_T'] = df['[sup 16[_T'] + df['14_16_t']

        df['[sup 12[_M'] = df['[sup 14[_M'] + df['12_14_m']
        df['[sup 12[_F'] = df['[sup 14[_F'] + df['12_14_f']
        df['[sup 12[_T'] = df['[sup 14[_T'] + df['12_14_t']

        df['[sup 10[_M'] = df['[sup 12[_M'] + df['[10_12[_M']
        df['[sup 10[_F'] = df['[sup 12[_F'] + df['[10_12[_F']
        df['[sup 10[_T'] = df['[sup 12[_T'] + df['[10_12[_T']

    return df[['N°','college','promotion','sans notes M','sans notes F','sans notes T',
           '[inf 7.5[_M','[inf 7.5[_F','[inf 7.5[_T','[7.5 9[_M','[7.5 9[_F','[7.5 9[_T',
           '[9 10[_M','[9 10[_F','[9 10[_T','[10_12[_M','[10_12[_F','[10_12[_T',
           '[sup 10[_M','[sup 10[_F','[sup 10[_T','[sup 12[_M','[sup 12[_F','[sup 12[_T',
            '[sup 14[_M','[sup 14[_F','[sup 14[_T','[sup 16[_M','[sup 16[_F','[sup 16[_T']]

