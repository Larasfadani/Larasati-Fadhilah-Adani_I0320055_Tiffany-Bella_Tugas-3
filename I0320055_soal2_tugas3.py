dict = {'Nama': 'Larasati Fadhilah Adani',
        'Hobi': ['Bermain game', 'Tidur', 'Dance'],
       'Sosmed': ['IG: @larasfadani', 'Fb: Larasati Fadhilah Adani', 'IG: @archiveslfa'],
        'Lagu kesukaan': ['Red carpet', 'Follow', 'Kazino'],
        'Makanan favorit': ['Nasi goreng', 'Mie goreng instan', 'Dimsum']
        }

dict['Hobi'][1] = 'Makan'
dict['Sosmed'][2] = 'ID Line: @larasfadani02'
del dict['Makanan favorit'][1]
del dict['Makanan favorit'][0]
dict['Hobi'].append('Mendengarkan lagu')