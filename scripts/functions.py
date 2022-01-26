# Importing important libraries
import numpy as np

# A function which will find the line between two points.
# @4_data_exploration.ipynb 
# @ Intercept And Slope
def get_line_equation(p1, p2):
    """
    Solve the system of equations:
    y1 = m*x1 + b
    y2 = m*x2 + b
    
    This translates to:
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m*x1
    
    Input:
    p1: first point [x1, y1]
    p2: second point [x2, y2]
    
    returns: slope, intercept
    """
    m = (p2[1] - p1[1]) / (p2[0] - p1[0]) # Slope
    b = p1[1] - m * p1[0] # Intercept
    return  m, b

# Removing the outliers
def remove_outliers(data, col):
      for x in col:
        q75,q25 = np.percentile(data.loc[:,x],[75,25])
        intr_qr = q75-q25
 
        max = q75+(1.5*intr_qr)
        min = q25-(1.5*intr_qr)
 
        data.loc[data[x] < min,x] = np.nan
        data.loc[data[x] > max,x] = np.nan
