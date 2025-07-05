
f = @(x) (1/(1-x))^(1/4);

u_list = zeros(100,1);
x = zeros(100,1);
for i = 1:100
    x(i) = rand();
    u_list(i) = f(x(i));
end

mu = mean(x);
sigma2 = var(x);

g = @(x) exp(-(-x - mu)^2/(2 * sigma2))/(sqrt(sigma2) * sqrt(2 *pi)); 

norm_list = zeros(100,1);
for i = 1:100
    x(i) = rand();
    norm_list(i) = g(x(i));
end





subplot(1,2,1)
histogram(u_list, 100)
subplot(1,2,2)
plot(norm_list, Color= "r")

