x_0 = .5; 
f_0 = exp(-2*x_0); %e^-2(.5)
fp = -2 *exp(-2*x_0); %first derivative at f_0 (-2*e^-2(.5))
i = -20:0.5:0; %array with step .5
h = 10.^i;
err = abs (fp - (exp(x_0+h) - f_0)./h ); %taylor approximation for derivative 
d_err = f_0/2*h; %approximation of error 
loglog (h,err,"-*"); %plot
hold on
loglog (h,d_err,"r-."); %plot with red dotted line
xlabel("h")
ylabel("Absolute error")
