clear;
T=2;
S0=50;
sigma = 0.3;
k = 52;
T = 2;
r = 0.05;
NT = 12;
dt = T/NT;
u = exp(sigma*sqrt(dt));
d = 1/u;
a = exp(r*dt);
p = (a-d)/(u-d);
ST = zeros(NT+1, 1);
Prob = zeros(NT+1, 1);
for j = 0:NT
    ST(j+1) = S0*(u^j)*(d^(NT-j));
    Prob(j+1) = nchoosek(NT,j)*(p^j)*((1-p)^(NT-j));
end
plot(ST,Prob,'-o');
xlim([0 400]);