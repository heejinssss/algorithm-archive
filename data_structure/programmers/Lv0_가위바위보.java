class Solution {
    public String solution(String rsp) {
        String answer = "";
        
        String[] rsp_arr = rsp.split("");
        
        for (String i : rsp_arr) {
            if (i.equals("2")) {
                answer += "0";
            } else if (i.equals("0")) {
                answer += "5";
            } else if (i.equals("5")) {
                answer += "2";
            }
        }

        return answer;
    }
}
