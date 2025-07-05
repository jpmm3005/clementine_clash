x_0 = 1.2; 
f_0 = sin(x_0); %sin(x) evaluated at x = 1.2
fp = cos(x_0); % cos(x) evaluated at x = 1.2
i = -20:0.5:0; % from -20 to 0 with step .5
h = 10.^i; % to display increasing values of h
err = abs (fp - (sin(x_0+h) - sin(x_0 -h))./h ); % f(x+h) - f(x-h) for error approx
err_2= abs (fp - (sin(x_0+h) - f_0)./h );
d_err = f_0/2*h; %discretization error
loglog (h,err,"-*")
hold on
loglog (h, err_2, "--")
xlabel("h")
ylabel("Absolute error")