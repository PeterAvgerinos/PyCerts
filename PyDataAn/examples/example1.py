import numpy as np
import pandas as pd

df = pd.DataFrame({'Certificates' : [8, 2, 4, 5],
                    'Time (in months)' : [16, 5, 9, 12]
                    })

df.index = ['Tom', 'Kris', 'Ahmad', 'Beau']
