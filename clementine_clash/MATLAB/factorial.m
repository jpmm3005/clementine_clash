e = exp(1);
n = 1:10;
Sn = sqrt(2* pi * n) .* ((n/e).^n);

for i

abs_error = abs(Fact_n - Sn);
relative_error = abs_error ./ Fact_n;

format short g;
[n; Fact_n; abs_error; relative_error]'