f = @(x) exp(2* x);

x = zeros(111,1);
y = zeros(111,1);
y_act = zeros(11,1)
h =.0001;
x(1) = 0;
y(1) = 1;

for i = 1:10000
    x(i+1) = h * (i);
    y(i+1) = f(x(i)) - 2*h*exp(2 *x(i));
    y_act = exp(-2* x(i)* i);
end

x;
y;

fplot(f, [0,1])
hold on 
plot(x,y, MarkerSize= 20,Color='black')
