import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {

        int[] num_rank = new int[rank.length];

        Arrays.fill(num_rank, 100); // 최댓값+1로 기본 세팅

        for (int i = 0; i < rank.length; i++) {
            if (attendance[i]) {
                num_rank[rank[i]-1] = i;
            }
        }
        
        int a = 0, b = 0, c = 0, count = 0;

        for (int num : num_rank) {
            if (num < 100 && count == 0) {
                a = num;
                count++;
            } else if (num < 100 && count == 1) {
                b = num;
                count++;
            } else if (num < 100 && count == 2) {
                c = num;
                count++;
            }
        }
        
        return (10000 * a) + (100 * b) + c;
    }
}
