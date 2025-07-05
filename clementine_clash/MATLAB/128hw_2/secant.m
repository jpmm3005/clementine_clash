x = zeros(100,1); %initialize null vector
x(1) = 7;  %initial value
x(2) = 8;  %initial value

f = @(x) x^3 - sinh(x) + 4*x.^2 + 6*x + 9;   %lambda function

y = zeros(100,1); %null vector
y(1) = f(x(1));
y(2) = f(x(2));

for i = 2:9 %10 iterations
    x(i+1) = x(i) - f(x(i) * (x(i) - x(i-1)))/(f(x(i)) - f(x(i-1))); %secant method
    y(i+1) = x(i+1); %append to vector
    y(i+1) = (f(x(i+1))); %append to vector
end



plot(x,y, '*-')
hold on
yline(0)
fplot(f)