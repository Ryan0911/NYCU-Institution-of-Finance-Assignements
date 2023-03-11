clear;
initialS = 50;
sigma = 0.3;
K=52;
T = 2;
r = Ｓ0.05;
q = 0;
d1 = (log(initialS/K)+(r-q+(sigma*sigma)/2)*T)/(sigma*sqrt(T));
d2 = (log(initialS/K)+(r-q-(sigma*sigma)/2)*T)/(sigma*sqrt(T));
nd1 = normcdf(d1,0,1);
nd2 = normcdf(d2,0,1);
ndp1 = (exp(-(d1^2)/2))/sqrt(2*pi);
ndp2 = (exp(-(d2^2)/2))/sqrt(2*pi);
delta = exp(-q*T)*(nd1-1);
gamma = (ndp1*exp(-q*T))/(initialS*sigma*sqrt(T));
theta = (-initialS*ndp1*sigma*exp(-q*T))/(2*sqrt(T)) + q*initialS*(1-nd1)*exp(-q*T) + r*K*exp(-r*T)*(1-nd2);
vega = initialS*sqrt(T)*ndp1*exp(-q*T);
rho = -K*T*exp(-r*T)*(1-nd2);
fprintf('Delta: %.6f\n',delta);
fprintf('Gamma: %.6f\n',gamma);
fprintf('Theta: %.6f\n', theta);
fprintf('Vega : %.6f\n',vega);
fprintf('Rho  : %.6f\n',rho);