clear;
T=2;
S0=50;
sigma = 0.3;
k = 52;
T = 2;
r = 0.05;
Type = 'a';%eu put options
NT = 12;
Option_Value_12 = HW3_311707006_Binomial_BS(S0,k,r,sigma,T,Type,NT);
NT = 52;
Option_Value_52 = HW3_311707006_Binomial_BS(S0,k,r,sigma,T,Type,NT);
NT = 252;
Option_Value_252 = HW3_311707006_Binomial_BS(S0,k,r,sigma,T,Type,NT);

BS = BS(S0,k,r,0,sigma,T, 'p');

fprintf('-----NT == 12-----\n')
fprintf('Option value by binomial: %.6f \nOption value by BS: %.6f ', Option_Value_12, BS)
fprintf('\n-----NT == 52-----\n')
fprintf('Option value by binomial: %.6f \nOption value by BS: %.6f ', Option_Value_52, BS)
fprintf('\n-----NT == 252-----\n')
fprintf('Option value by binomial: %.6f \nOption value by BS: %.6f ', Option_Value_252, BS)