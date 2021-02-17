# https://programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):
    answer = 0
    loc = 0;
    
    for i in range(0, k):
        for j in range(0, len(food_times)):
            if food_times[loc] != 0:
                food_times[loc] -= 1;
                loc = (loc + 1) % len(food_times);  
                break;
            else:
                loc = (loc + 1) % len(food_times);    
             
    while(True):
        if food_times[loc] != 0:
            break;
        loc = (loc + 1) % len(food_times); 
            
    answer = loc + 1;
    return answer