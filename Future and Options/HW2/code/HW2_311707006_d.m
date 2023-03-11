clear;
NE = 500;
MoteCarlo_Options = zeros(1,NE);
prompt = "Please input your number of sample paths: ";
flag = input(prompt);
for j = 1:NE
    while(true)
        if(flag == 100)
            HW2_311707006_100;
            break;
        elseif(flag == 10000)
            HW2_311707006_10000;
            break;
        elseif(flag == 1000000)
            HW2_311707006_1000000;
            break;
        end
        fprintf("Please try again. input a correct number. (100, 10000, 1000000)\n");
        prompt = "Please input your number of sample paths: "; 
        flag = input(prompt);
    end
    MoteCarlo_Options(j) = Mean_Option;
    if(mod(j, 100)==0)
        fprintf("iteration: %d\n", j)
    end
end
Experiment_Mean_OP = mean(MoteCarlo_Options)
Experiment_SD_OP = std(MoteCarlo_Options)
Mean_Option = mean(Option_Price);
fprintf("Mean: %.2f, Standard deviation: %.2f", Experiment_Mean_OP, Experiment_SD_OP)
