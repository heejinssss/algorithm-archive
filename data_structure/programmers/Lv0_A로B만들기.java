import java.util.*;

class Solution {
    public int solution(String before, String after) {
        
        String[] b_arr = before.split("");
        String[] a_arr = after.split("");

        Arrays.sort(b_arr);
        Arrays.sort(a_arr);

        /*
        String b = String.join("", b_arr);
        String a = String.join("", a_arr);

        return b.equals(a) ? 1 : 0;
        */
        
        return Arrays.equals(a_arr, b_arr) ? 1 : 0;
    }
}
