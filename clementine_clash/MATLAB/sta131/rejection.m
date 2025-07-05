Af = @(x) x^4 + 1/4
x = 1:10;
T = zeros(10,1)
U = zeros(10,1)
accept = zeros(10,1)
domain  = zeros(10,1)


for i = 1:10
   T(i) = -1 + (1 +1) * rand()
   U(i) = rand()
end

for i= 1:10
    if U(i) <= f(T(i))
        accept(i) = U(i);
        domain(i) = T(i)
    end
end

accept = nonzeros(accept)
domain = nonzeros(domain)

subplot(1,2,1)
hold on
plot(domain, accept, '*r')   % Accepted points
xlim([-1 1])
ylim([0 1])                  % Adjusted for the range of f(x)
fplot(f, [-1 1], 'b')        % Plot the function f(x)
title('Accepted Samples')
hold off

subplot(1,2,2)
hold on
plot(T, U, '*r')             % All sampled points
fplot(f, [-1 1], 'b')        % Plot the function f(x)
xlim([-1 1])
ylim([0 1])
title('All Samples')
hold off
