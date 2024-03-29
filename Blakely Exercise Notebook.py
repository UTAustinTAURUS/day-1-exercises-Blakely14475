
# coding: utf-8

# ## Exercises
# 
# This will be a notebook for you to work through the exercises during the workshop. Feel free to work on these at whatever pace you feel works for you, but I encourage you to work together! Edit the title of this notebook with your name because I will ask you to upload your final notebook to our shared github repository at the end of this workshop.
# 
# Feel free to google the documentation for numpy, matplotlib, etc.
# 
# Don't forget to start by importing any libraries you need.

# In[17]:


import numpy as np
import astropy
import matplotlib.pyplot as plt
from scipy import integrate


# ### Day 1
# 
# #### Exercise 1
# 
#    A. Create an array with 10 evenly spaced values in logspace ranging from 0.1 to 10,000.
# 
#    B. Print the following values: The first value in the array, the final value in the array, and the range of 5th-8th values.
# 
#    C. Append the numbers 10,001 and 10,002 (as floats) to the array. Make sure you define this!
# 
#    D. Divide your new array by 2.
# 
#    E. Reshape your array to be 3 x 4. 
# 
#    F. Multiply your array by itself.
#     
#    G.  Print out the number of dimensions and the maximum value.

# In[18]:


logarray = np.logspace(np.log10(0.1), np.log10(10000), 10) #i have created an array with 10 evenly spaced values
#between 0.1 and 10000
print(logarray[0], logarray[9], logarray[4:7]) #i want to see the first value, the 10th value, and values 5-8
logappend = [10001, 10002] #creating a new list to append onto the array
print(logappend) #just wanna make sure that worked...

logarrayappend = np.append(logarray, logappend) #creating a new array with the appended list. i realized later that 
#logarrayappend is a terrible name for an array cause it takes a really long time to type
print(logarrayappend) #making sure that worked again lol

arrayover2 = logarrayappend / 2 #divide the whole dang thing in half
reshaped = arrayover2.reshape(3, 4) #reshaping it into a 3x4 matrix. notably, i printed it before reshaping it, and it
#looks like the notebook already wanted it to be a 3x4. whatever
print(reshaped) #making sure that worked

logmult = reshaped**2 #gonna name a brand new array which is the square of my other arrays...

print(logmult) #always makin sure things worked
print(logmult.ndim) #okay so the dimension is one..this doesnt make a lot of sense. multiplying logarrayappend by itself is a
#dot product, then okay we'll get a single dimension scalar answer. but when we print logmult, it shows a 3x4 matrix.
#and we're looking for the maximum value, shown below. that only makes sense if multiplying them was the act of a cross
#product. but the cross product of a vector with itself is zero...
#It turns out that this act of multiplication is simply multiplying each entry by itself and generating a 3x4 matrix 
#populated with those products. print(logmult.ndim) results in a 2 being printed because that's the dimension of the
#vectors that make up that matrix.

np.max(logmult)


# ### Day 2

# #### Exercise 1
# 
#    A. Create an array containing the values 4, 0, 6, 5, 11, 14, 12, 14, 5, 16.
#    B. Create a 10x2 array of zeros.
#    C. Write a for loop that checks if each of the numbers in the first array squared is less than 100. If the statement is true, change that row of your zeros array to equal the number and its square. Hint: you can change the value of an array by stating "zerosarray[i] = [a number, a number squared]". 
#    D. Print out the final version of your zeros array.
#     
# Hint: should you loop over the elements of the array or the indices of the array?

# In[19]:


array1 = np.array([4, 0, 6, 5, 11, 14, 12, 14, 5, 16]) #we populate our array
print(array1)

zeroarray = np.zeros((10, 2)) #we create a 10x2 matrix full of zeros
print(zeroarray)

for n in range(len(array1)): #there are very specific reasons to use n in range(len(array1)) instead of n in array1
    #n in array1 focuses on the element (i.e. 4, 0, 6,...), whereas n in range(len(array1)) sorts and works the 
    #numbers by their index (i.e. 0, 1, 2, 3,...) in order. what we care about is that the matrix we get after all this
    #hard work have the same elements in the same order as we started. For that we want to focus on their indices
    if array1[n]**2 < 100: #we have to specify that we want the element, not the index, squared. n**2 would square the
        #index, and not the element itself
        zeroarray[n] = [ array1[n], array1[n]**2 ] #we use n again to specify that for the nth index of array1, 
        #modify the nth index of zeroarray
        
print(zeroarray) #make sure that we print zeroarray outside of the for loop, or else it will print it each time it runs
#the loop


# #### Exercise 2
#     
#    A. Write a function that takes an array of numbers and spits out the Gaussian distribution. Yes, there is a function for this in Python, but it's good to do this from scratch! This is the equation:
#     
# $$ f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp{\frac{-(x - \mu)^2}{2\sigma^2}} $$
# 
#     (Pi is built into numpy, so call it as np.pi.)
# 
#    B. Call the function a few different times for different values of mu and sigma, between -10 < x < 10.
#     
#    C. Plot each version, making sure they are differentiated with different colors and/or linestyles and include a legend. Btw, here's a list of the customizations available in matplotlib:
#     
#     https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.plot.html
#     
#     https://matplotlib.org/gallery/color/named_colors.html
#     
#    D. Save your figure.
#     
# If you have multiple lines with plt.plot(), Python will plot all of them together, unless you write plt.show() after each one. I want these all on one plot.

# In[20]:


#A 
fig = plt.figure()
def distro(p, x, s, m):
    y = (1 / (s * ((2 * p)**(1/2)))) * np.exp((-((x - m)**2)) / (2 * (s**2)))
    return y

#B
# -10 < x < 10 in all of these. what values do i want to give sigma? what values can sigma have? s =/= 0.
#even if the difference of x - mu is a negative number, it is a squared value, multiplied by negative one. The 
#denominator inside the exponential function is always positive (sigma is squared), so the term inside the exponential
#will *always* be negative, dropping off towards the limit of y = 0. Note that there anywhere x = mu, exp(0) = 1, 
#and as a result, f(x) = 1/(sigma * sqrt(2 * pi))
x = np.linspace(-10, 10, 100) #somehow this line got deleted after my plot was complete, completely ruining the code
y_value1 = distro(np.pi, np.linspace(-10, 10, 100), 1, 1)
y_value2 = distro(np.pi, np.linspace(-10, 10, 100), 2, 2)
y_value3 = distro(np.pi, np.linspace(-10, 10, 100), 3, 3)
y_value4 = distro(np.pi, np.linspace(-10, 10, 100), 4, 4)
y_value5 = distro(np.pi, np.linspace(-10, 10, 100), 5, 5)


#C
plt.plot(x, y_value1, 'g-', label = '(σ, μ) = (1, 1)') #Python 3 & Latex 2 both support Greek alphabet, which is nice
plt.plot(x, y_value2, 'b-', label = '(σ, μ) = (2, 2)')
plt.plot(x, y_value3, 'r-', label = '(σ, μ) = (3, 3)')
plt.plot(x, y_value4, 'orange', linestyle = '-', label = '(σ, μ) = (4, 4)')
plt.plot(x, y_value5, 'purple', linestyle = '-', label = '(σ, μ) = (5, 5)')
plt.xlabel('x-axis') #i actually want to make some further changes to this to spruce it up. for instance, i'd like a 
#legend showing that the sigma and mu values vary for each one. But I did this in only an hour and a half this morning
#and i'm pretty proud of it
plt.ylabel('y-axis')
plt.title('Gaussian Distribution Plot')
plt.legend(loc='upper right', frameon=True)

#D
fig.savefig('Blakely_Gaussian_Plot.png')
plt.show()


# ### Day 3
# 
# #### Exercise 1
# 
# There is a file in this directory called "histogram_exercise.dat" which consists of of randomly generated samples from a Gaussian distribution with an unknown $\mu$ and $\sigma$. Using what you've learned about fitting data, load up this file using np.genfromtxt, fit a Gaussian curve to the data and plot both the curve and the histogram of the data. As always, label everything, play with the colors, and choose a judicious bin size. 
# 
# Hint: if you attempt to call a function from a library or package that hasn't been imported, you will get an error.

# In[22]:


column1 = np.genfromtxt('histogram_exercise.dat').T

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import optimize as opt 
import math

# THE ORDER MATTERS HERE: mu, sig, f0 is index 0, 1, 2 (x doesn't get fit)
#def gauss2(x, mu, sig, f0):
  #  exp = np.exp(- (x - mu)**2 / (2 * sig**2) )
 #   return f0 * exp

#bfpars, covar = opt.curve_fit(gauss2, p0=[7, 2, 2e+2])
#mu and sigma are unknown, and i dont know what the column in the histogram is. i'm guessing it's f0?

#mu, sigma = norm.fit(column1)
fig = plt.figure()
mu, sigma = norm.fit(column1) #this tells python to attempt to fit a μ & σ to a table of data. python already knows
#to attempt a fit for them in that order, and we are simply telling it to use "mu" & "sigma" to represent those 
#variables in the future. the command norm.fit(column1) finds a mu & sigma, but does not assign them variables
print(mu, sigma)

plt.hist(column1, bins=20, density=True, label='histogram') #we are only plotting a histogram of one column, here an array of values
#which we imported
xarray = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000) #we need three columns to fit a probability density function
#fit the pdf to a range of values associated with our histogram, namely the mu & sigma values we found
gauss_model = norm.pdf(xarray, mu, sigma)
plt.xlim(-5, 15)
plt.plot(xarray, gauss_model, label='fit')

plt.legend(loc='upper right', frameon=True)
plt.xlabel('Wavelength')
plt.ylabel('Flux')
plt.title('Gaussian Fit, μ ≈ 5, σ ≈ 2')

fig.savefig('Blakely_Histogram_Fit')
plt.show()

#here's a completely different way to map these...probably not a great idea unless you already know its gaussian
gauss_model_test = norm.pdf(column1, mu, sigma)
plt.plot(column1, gauss_model_test, 'o')


# #### Exercise 2
# 
# Create a 1D interpolation along these arrays. Plot both the data (as points) and the interpolation (as a dotted line). Also plot the value of the interpolated function at x=325. What does the function look like to you?

# In[23]:


x = np.array([0., 50., 100., 150., 200., 250., 300., 350., 400., 450., 500])
y = np.array([0., 7.071, 10., 12.247, 14.142, 15.811, 17.321, 18.708, 20., 21.213, 22.361])

plt.plot(x, y, 'o') #this is simply a plot of the arrays provided

from scipy.interpolate import interp1d
interp = interp1d(x, y) 

xnew = np.linspace(0, 500, 10000)
ynew = interp(xnew) 

print(interp(x=325)) #the interpolation of x at 325 is 18.0145. this looks correct based on the chart
#now i need to find a way to plot the chart

z = 325 #hard coding numbers is a bad idea. assign z = 325, and then plot z
t = np.array([z])
e = np.array([interp(x=z)])

plt.plot(xnew, ynew, '--')
plt.plot(x, y, 'ob', alpha=0.25)
dotplot = plt.plot(t, e, 'or', markersize=6) #single points default to a line, so we need to tell it to display the
#point as a dot with 'o'
plt.axvline(x=z)
plt.axhline(y=interp(x=z)) 

plt.show() #wanted to make sure you could see the point i found.


# ### Day 4
# 
# #### Exercise 1
# 
# Let's practice some more plotting skills, now incorporating units. 
# 
# A. Write a function that takes an array of frequencies and spits out the Planck distribution. That's this equation:
# 
# $$ B(\nu, T) = \frac{2h\nu^3/c^2}{e^{\frac{h\nu}{k_B T}} - 1} $$
# 
# This requires you to use the Planck constant, the Boltzmann constant, and the speed of light from astropy. Make sure they are all in cgs. 
#     
# B. Plot your function in log-log space for T = 25, 50, and 300 K. The most sensible frequency range is about 10^5 to 10^15 Hz. Hint: if your units are correct, your peak values of B(T) should be on the order of 10^-10. Make sure everything is labelled. 

# In[ ]:


# solution here


# #### Exercise 2
# 
# Let's put everything together now! Here's a link to the full documentation for FITSFigure, which will tell you all of the customizable options: http://aplpy.readthedocs.io/en/stable/api/aplpy.FITSFigure.html. Let's create a nice plot of M51 with a background optical image and X-ray contours overplotted.
# 
# The data came from here if you're interested: http://chandra.harvard.edu/photo/openFITS/multiwavelength_data.html
# 
# A. Using astropy, open the X-RAY data (m51_xray.fits). Flatten the data array and find its standard deviation, and call it sigma.
# 
# B. Using aplpy, plot a colorscale image of the OPTICAL data. Choose a colormap that is visually appealing (list of them here: https://matplotlib.org/2.0.2/examples/color/colormaps_reference.html). Show the colorbar. 
# 
# C. Plot the X-ray data as contours above the optical image. Make the contours spring green with 80% opacity and dotted lines. Make the levels go from 2$\sigma$ to 10$\sigma$ in steps of 2$\sigma$. (It might be easier to define the levels array before show_contours, and set levels=levels.)

# In[ ]:


# solution here

