import java.math.*;

class Solution {
    public String solution(String a, String b) {

        /* 시간 이슈
        String answer = "";

        BigInteger a_num = new BigInteger(a);
        BigInteger b_num = new BigInteger(b);

        answer = a_num.add(b_num).toString();

        return answer;
        */

        StringBuilder sb = new StringBuilder();
        
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        
        while (i >= 0 || j >= 0 || carry > 0) {
            int sum = carry;
            
            if (i >= 0) sum += a.charAt(i--) - '0';
            if (j >= 0) sum += b.charAt(j--) - '0';
            
            sb.append(sum % 10);
            carry = sum / 10;
        }
        
        return sb.reverse().toString();
    }
}
