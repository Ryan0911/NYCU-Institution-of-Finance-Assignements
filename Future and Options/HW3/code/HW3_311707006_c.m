clear;
T=2;
S0=50;
sigma = 0.3;
k = 52;
T = 2;
r = 0.05;
Type = 'e';%eu put options
N_steps = 252;
Option_Value = zeros(N_steps, 1);
for i = 1:N_steps
    NT = i;
    Option_Value(i) = HW3_311707006_Binomial_BS(S0,k,r,sigma,T,Type,NT);
end
BS = BS(S0,k,r,0,sigma,T, 'p');
BS_plot = BS*ones(N_steps, 1);
plot(1:N_steps, Option_Value, 1:N_steps, BS_plot);
xlim([0 250]);
