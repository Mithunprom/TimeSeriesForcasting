# TimeSeriesForcasting

<h2>Objective</h2>
In this challenge, we practice predicting time series. 
<h3>Task</h3>
You are given the web traffic data for a particular website, which is measured in terms of user sessions. You are provided with the number of sessions for a time series of  consecutive days starting from . Your task is to predict the number of sessions for the next  days.

<h2>Instruction</h2>

<h2>Methodology</h2>
Lets print the data to see if there is any pattern, trend , seasonality .
<img src="img_girl.jpg" alt="Girl in a jacket">

<p1>Some distinguishable patterns appear when we plot the data. The time series has an obvious seasonality pattern.
<p2>
One of the most common methods used in time series forecasting is known as the ARIMA model, which stands for AutoregRessive Integrated Moving Average. ARIMA is a model that can be fitted to time series data in order to better understand or predict future points in the series.
<p3>There are three distinct integers (p, d, q) that are used to parametrize ARIMA models. Because of that, ARIMA models are denoted with the notation ARIMA(p, d, q). Together these three parameters account for seasonality, trend, and noise in datasets. 
<p2>We will use a “grid search” to iteratively explore different combinations of parameters, or each combination of parameters, we fit a new seasonal ARIMA model with the SARIMAX() function from the statsmodels module and assess its overall quality. Once we have explored the entire landscape of parameters, our optimal set of parameters will be the one that yields the best 
<p2>performance for our criteria of interest. Let’s begin by generating the various combination of parameters that we wish to assess:
Using grid search, we have identified the set of parameters that produces the best fitting model to our time series data. We can proceed to analyze this particular model in more depth. We’ll start by plugging the optimal parameter values into a new SARIMAX model.
When fitting seasonal ARIMA models (and any other models for that matter), it is important to run model diagnostics to ensure that none of the assumptions made by the model have been violated. The plot_diagnostics object allows us to quickly generate model diagnostics and investigate for any unusual behavior.    
<img src="img_girl.jpg" alt="Girl in a jacket">
 <p4> In this case, our model diagnostics suggests that the model residuals are normally distributed based on the following:
<ul>
<li>In the top right plot, we see that the red KDE line follows closely with the N(0,1) line (where N(0,1)) is the standard notation for a normal distribution with mean 0 and standard deviation of 1). This is a good indication that the residuals are normally distributed.</li>
<li>The qq-plot on the bottom left shows that the ordered distribution of residuals (blue dots) follows the linear trend of the samples taken from a standard normal distribution with N(0, 1). Again, this is a strong indication that the residuals are normally distributed.</li>
<li>The residuals over time (top left plot) don’t display any obvious seasonality and appear to be white noise. This is confirmed by the autocorrelation (i.e. correlogram) plot on the bottom right, which shows that the time series residuals have low correlation with lagged versions of itself.</li>
  
<h2>Validating Forecasts  </h2>
We have obtained a model for our time series that can now be used to produce forecasts. We start by comparing predicted values to real values of the time series, which will help us understand the accuracy of our forecasts. The get_prediction() and conf_int() attributes allow us to obtain the values and associated confidence intervals for forecasts of the time series. We requires the forecasts to start at '2013-10-01'. The prediction curve is shown below:
<img src="img_girl.jpg" alt="Girl in a jacket">
Also for better view, the predicted region can be ploted deparetly. where er can see that the predcition is quite well considering the sopisticated time series relationship.
<img src="img_girl.jpg" alt="Girl in a jacket">

