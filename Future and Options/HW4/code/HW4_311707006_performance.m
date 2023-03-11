function  performance = HW4_311707006_performance(rebalance)
T = 20/52;
dt = rebalance/52;
mu = 0.13;
sigma = 0.2;
initialS = 49;
numberS = 1000; % 1000 sample paths
dS = zeros(numberS,T/dt);
dz = randn(numberS, T/dt) * sqrt(dt);
S = zeros(numberS, T/dt + 1);
Delta = zeros(numberS, T/dt + 1);
Shares_purchased = zeros(numberS, T/dt + 1);
Cost_of_shares = zeros(numberS, T/dt + 1);
Cumulative_cost_including = zeros(numberS, T/dt + 1);
Interest_cost = zeros(numberS, T/dt + 1);
Hedge_cost = zeros(numberS,1);
K = 50;
r = 0.05;
for i = 1:numberS
    S(i,1) = initialS;
    d1 = (log(S(i,1)/K)+(r+(sigma*sigma)/2)*T)/(sigma*sqrt(T));
    Delta(i, 1) = normcdf(d1,0,1);
    Shares_purchased(i, 1) = Delta(i, 1) * 100000;
    Cost_of_shares(i, 1) = S(i, 1) * Shares_purchased(i, 1);
    Cumulative_cost_including(i, 1) = Cost_of_shares(i, 1);
    Interest_cost(i, 1) = Cumulative_cost_including(i, 1) * (r*dt);
    for j = 1:T/dt
        dS(i,j) = S(i, j)*(mu*dt + sigma*dz(i,j));
        S(i, j+1) = S(i,j)+dS(i,j);%下一期股價
        d1 = (log(S(i,j+1)/K)+(r+(sigma*sigma)/2)*(T-dt*j))/(sigma*sqrt(T-dt*j));
        Delta(i, j+1) = normcdf(d1,0,1);
        Shares_purchased(i, j+1) = (Delta(i, j+1)-Delta(i, j)) * 100000;
        Cost_of_shares(i, j+1) = S(i, j+1) * Shares_purchased(i, j+1);
        Cumulative_cost_including(i, j+1) = Cumulative_cost_including(i, j) + Interest_cost(i, j) + Cost_of_shares(i, j+1);
        Interest_cost(i, j+1) = Cumulative_cost_including(i, j+1) * (r*dt);
    end
    if S(i,j+1)>=K % in the money
        Hedge_cost(i) = Cumulative_cost_including(i, j+1) - (K*100000);
    else % out of the money
        Hedge_cost(i) = Cumulative_cost_including(i, j+1);
    end

end
std_hedge = std(Hedge_cost);
BS_call_price = BS (initialS,K,r,0,sigma,T,'c') * 100000;
performance = std_hedge/BS_call_price;