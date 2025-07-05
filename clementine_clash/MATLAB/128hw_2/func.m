function [y] = f(x) 

f(x) = ((x)-1).^(x) * exp(x);

end

function [yp] = g(x)

g(x) = 2 * (x)*exp(x) - 2*(exp(x)) + ((x)-1).^2 * exp(x); 

end