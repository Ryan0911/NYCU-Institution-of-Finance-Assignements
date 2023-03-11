T = 1;
N = 52;
dt = T/N;
mu = 0.15;
sigma = 0.3;
initialS = 100;
numberS = 10000; % 10000 sample paths
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

nbins = 100;
hist(S(:, N*T + 1), nbins);