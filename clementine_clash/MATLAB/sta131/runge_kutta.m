f = @(t) (exp(t)*sin(t) + exp(t)*cos(t)) -1;
y_0 = 1


h = 0.01;
x = zeros(300);
x(1) = 0;
y = zeros(300);
y(1) = 1;


for i = 1:299
    x(i+1) = h * i;
    y(i+1) = f(x(i))*(1-h) + 2*h*cos(x(i)) + h^2 *(1/2) *( (f(x(i)) - 2*cos(x(i)) )^2) - (h^3 / 3) * cos(x(i)) - h^3 *((2*cos(x(i)) - f(x(i)))^3) - h^3 * ((f(x(i)) -2*cos(x(i)))^2)  + h^3 * (f(x(i)) - 2*cos(x(i))^2)*(2*cos(i)) - f(x(i));

end

fplot(f, XRange=[0,pi])
hold on
plot(x,y,MarkerSize=20, color='r')

