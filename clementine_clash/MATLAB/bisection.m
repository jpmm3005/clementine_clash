
b = 20;
a = 0;

f_a = (a)^3 - 30* (a^2) + 2552;
f_b = (b)^3 - 30* (b^2) + 2552;

%choose atol to be 0.01
% choose n st abs(a-b)/2 * 1/2^n < atol

atol = 0.000000001;
n = log2(10/atol);
n = ceil(n);

sign = f_a * f_b;
for i = 1:n
    p = (a+b)/2;
    f_p =  (p)^3 - 30 * (p^2) + 2552;
    if (f_a * f_p  < 0)
        b = p;
        f_b = f_p;
    else
        a = p;
        f_a = f_p;
    end
        p = (a+b)/2;
    
end

x = 0:1:20;
y = (x).^3 - 30 * (x.^2) + 2552;
plot(x,y)
hold on;
yline(0)
plot(p ,0, 'r.', 'MarkerSize', 30)
hold off