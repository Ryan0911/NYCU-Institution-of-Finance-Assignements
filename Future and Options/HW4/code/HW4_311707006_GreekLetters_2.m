clear;
S0 = 50;
sigma = 0.3;
K = 52;
T = 2;
r = 0.05;
q = 0;
NT = T*252;

dt = T/NT;
u = exp(sigma*sqrt(dt));
d = 1/u;
a = exp((r-q)*dt);
p = (a-d)/(u-d);

f = zeros(NT+1,NT+1);

for j = 0:NT
    f(NT+1, j+1) = max(K-S0*(u^j)*(d^(NT-j)),0);
end

%Backward
for i = (NT-1):-1:0
    for j = 0:i
            f(i+1, j+1) = max(0, exp(-r*dt)*(p*f(i+2,j+2)+(1-p)*f(i+2, j+1)));
    end
end


delta = (f(2,2)-f(2,1))/(S0*(u-d));
gamma = ((f(3,3)-f(3,2))/(S0*(u^2-1))-(f(3,2)-f(3,1))/(S0*(1-d^2)))/(0.5*(S0*(u^2-d^2)));
theta = (f(3,s2)-f(1,1))/(2*dt);
vega = HW3_311707006_Binomial_BS (S0, K, r, 0.3001, T, 'e', NT) - HW3_311707006_Binomial_BS (S0, K, r, sigma, T, 'e', NT);
rho = HW3_311707006_Binomial_BS (S0, K, 0.0501, sigma, T, 'e', NT) - HW3_311707006_Binomial_BS (S0, K, r, sigma, T, 'e', NT);
fprintf('Delta: %.6f\n',delta);
fprintf('Gamma: %.6f\n',gamma);
fprintf('Theta: %.6f\n', theta);
fprintf('Vega : %.6f\n',vega);
fprintf('Rho  : %.6f\n',rho);