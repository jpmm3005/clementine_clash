x(1) = 5;  %initial value
x(2) = 6;  %initial value

f = @(x) x^3 - sinh(x) + 4*x.^2 + 6*x + 9;   %lambda function

x_list = zeros(20,1); %null vector
x_list(1) = 5;       
x_list(2) = 6;

y_list = zeros(20,1); %null vector
y_list(1) = f(x(1));
y_list(2) = f(x(2));

for i = 2:19
    x(i+1) = double(x(i) - (f(x(i) * x(i) - x(i-1)))/(f(x(i)) - f(x(i-1))) ); %secant method
    x_list(i+1) = x(i+1); %append to vector
    y_list(i+1) = double(f(x(i+1))); %append to vector
end

%slope_0 = f(x(2)) - f(x(1))/(x(2) - x(1)); %slope of first secant line 
%y_0 = y_list(1);
%x_0 = x_list(1);
%g = @(x) slope_0*(x - x_0) + y_0; %equation of secant line

%slope_1 =  f(x(3)) - f(x(2))/(x(3) - x(1)); %slope of second secant line 
%y_1 = y_list(2);
%x_1 = x_list(2)
%g2 = @(x) slope_1*(x - x_1) + y_1; %equation of secant line

%y_list
x_list

