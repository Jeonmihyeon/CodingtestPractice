class Solution {
    public int solution(int[] num_list) {
        int m = num_list.length;
        int answer = 1;
        
        if (m >= 11){
            answer -= 1;
            for (int i = 0;i<m;i++)
                answer += num_list[i];
        }
        else{
            for (int i = 0;i<m;i++)
                answer *= num_list[i];        
        }
               
        return answer;
    }
}