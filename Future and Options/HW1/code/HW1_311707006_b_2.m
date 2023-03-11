T = 1;
N = 252;
dt = T/N;
mu = 0.15;
sigma = 0.3;
initialS = 100;
numberS = 10; % 10 sample paths
dS = zeros(numberS,N*T);
dz = randn(numberS, N*T) * sqrt(dt);
S = zeros(numberS, N*T + 1);
for i = 1:numberS
    S(i,1) = initialS;
    for j = 1:N*T
        dS(i,j) = S(i, j)*(mu*dt + sigma*dz(i,j));
        S(i, j+1) = S(i,j)+dS(i,j);
    end
end
Time = 0:dt:T;
plot(Time, S)
