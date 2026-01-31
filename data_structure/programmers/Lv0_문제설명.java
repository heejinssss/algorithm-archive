import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public String solution(int q, int r, String code) {
        String answer = "";

        String[] codeArr = code.split("");

        for (int i = 0; i < codeArr.length; i++) {
            answer = i % q == r ? answer + codeArr[i] : answer;
        }

        return answer;
    }
}
