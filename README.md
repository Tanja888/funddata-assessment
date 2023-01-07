# Fundamentals of Data Analysis Assessment
# About the Assessment
The purpose of this assessment was to explore different concepts in data analysis with practical examples. It contains two parts, one with the practical exercises for various topics relevant for data analysis and the other one describing and visualising the main concepts of the normal distribution. 

# Repository
The repository contain the folder practicals with five notebooks and two csv files with data sets, normal distribution notebook, images, Readme file and .gitignore
Repository URL: https://github.com/Tanja888/funddata-assessment 

# Technologies
Python 3.9.13

# Running the Jupyter Notebook
Python is necessary in order to run the Jupyter Notebook on the user’s local machine. The notebook can be started through the command line in Terminal for Linux and Mac or Command Prompt for Windows after navigating into the correct directory. The github repository can be cloned through the terminal. Once the notebook opens in the browser it is easy to navigate through its dashboard with all the files it contains. 

# Normal Distribution Notebook
To open the Normal Distribution notebook, please follow the link below: 
https://github.com/Tanja888/funddata-assessment/blob/main/normal-distribution.ipynb 

# Setup
Libraries used for the analysis:
```python
    import urllib.request
    import random
    import numpy as np
    import math
    import matplotlib.pyplot as plt
    import seaborn as sns
    import scipy.stats as ss
    from scipy.stats import norm, skew, kurtosis
    import scipy.special
    import statistics as st
    import pandas as pd
    import re
```

# Notebooks
I The first part is ‘practicals’ folder with five notebooks:  
 1.	In the Information notebook we used different Python functionalities to generate characters based on the certain conditions. In the second exercise it was explained why the log of 0 is undefined.  
 2.	In the Randomness notebook, formula for the binomial coefficient was shown, the plots of three different types of distributions were plotted: Poisson, Chi-Square and Gamma distribution.  
 3.	Bias notebook contains three real-world examples of cognitive bias and the visual representation of changing the value of standard deviation depending on the sample size.   
 4.	In the Outliers notebook we recreated box plots for the morley data set taken from Wikipedia, as well as the box plots for the numerical variables of the Fisher’s Iris Data set. 
 5.	Cleansing notebook shows the use of Regular Expressions in Python.   

II The second part of the assessment is the Normal distribution notebook 

The main concepts of the normal distribution were described and visualised. First, the definition was given together with the probability density function. Then the parameters mu and sigma were described with the plots for different sigma values. 

![sigma](https://github.com/Tanja888/funddata-assessment/blob/main/images/sigma.png)

The difference between the standard deviation and the standard error was explained as well as the idea of the z-scores.   
Empirical or the 68-95-99.7 rule was plotted for easier comprehension showing what percentage of values fall under the distribution’s curve if we look at the standard deviation. 
![empirical_rule](https://github.com/Tanja888/funddata-assessment/blob/main/images/empirical_rule.png)

Three measures of central tendency (MCT) were described, mean, median and the mode and in the visual part the affect that the outliers have on the mean.   
![mct](https://github.com/Tanja888/funddata-assessment/blob/main/images/mct.png)

For the Central limit theorem (CLT) we took an example from DataCamp to show how the sampling distribution of the means resembles more to the normal distribution in case of larger number of samples. 

In the end, the measures of skewness and kurtosis were touched upon, the differences between the three types of kurtosis were described while the plot was used to show three types of skewness.
![skewness](https://github.com/Tanja888/funddata-assessment/blob/main/images/skewness.png)  

# Conclusion
The practical exercises in the first part of the assessment gave a good idea of what aspects exist and should be considered while analysing data, from understanding the ideas of randomness and bias to using regular expressions for easier data preparation and cleaning. Describing the concepts of the normal distribution through examples and visual representations was a useful reminder of its importance in statistics and data analysis. 


[def]: https://github.com/Tanja888/funddata-assessment/blob/main/images/sigma.png
[def2]: https://github.com/Tanja888/funddata-assessment/blob/main/images/empirical_rule.png
[def3]: https://github.com/Tanja888/funddata-assessment/blob/main/images/mct.png
[def4]: https://github.com/Tanja888/funddata-assessment/blob/main/images/skewness.png