#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers) {
    int answer = 0;
    int max = 0, s_max = 0;

    for (int i: numbers){
        if(max <= i){
            s_max = max;
            max = i;
        }
        else if(s_max <= i){
            s_max = i;
        }
    }
    answer = max * s_max;
    return answer;
}