sigma = 0.3;
K = 52;
T = 2;
r = 0.05;
NP = 1000000;
S0 = 50;
S = zeros(1, NP);
Option_Price = zeros(1, NP);
rn = randn(1, NP);
for i = 1:NP
    S(i) = S0*exp((r-(sigma^2)/2)*T + sigma*rn(i)*sqrt(T));
    Option_Price(i) = exp(-r*T) * max((K-S(i)), 0);
end

Mean_Option = mean(Option_Price);
%SD_Option = std(Option_Price);
%Std_Error = SD_Option / sqrt(NP);
%fprintf("95/percent Confidence is (%.2f, %.2f)", Mean_Option - (1.96*Std_Error),Mean_Option + (1.96*Std_Error))
%fprintf('\nOption price: %.2f', Mean_Option)
%nbins = 100;
%hist(S(:,:), nbins);
