import java.util.Arrays;

class Solution {
    public int solution(String[] strArr) {
        int[] countArr = new int[30];
        
        for (String str : strArr) {
            countArr[str.length()-1] += 1;
        }

        Arrays.sort(countArr);

        return countArr[29];
    }
}
