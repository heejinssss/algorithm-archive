class Solution {
    public String solution(String code) {
        String answer = "";
        String ret = "";
        int mode = 0;

        /*
        for (int idx = 0; idx < code.length(); idx++) {
            if (mode == 0) {
                if (code.substring(idx, idx+1).equals("1")) {
                    mode = 1;
                } else {
                    ret = idx % 2 == 0 ? ret + code.charAt(idx) : ret;
                }
            } else if (mode == 1) {
                if (code.substring(idx, idx+1).equals("1")) {
                    mode = 0;
                } else {
                    ret = idx % 2 != 0? ret + code.charAt(idx) : ret;
                }
            }
        }
        */

        // /*
        for (int idx = 0; idx < code.length(); idx++) {
            if (mode == 0) {
                if (code.charAt(idx) == '1') {
                    mode = 1;
                } else {
                    ret = idx % 2 == 0 ? ret + code.charAt(idx) : ret;
                }
            } else if (mode == 1) {
                if (code.charAt(idx) == '1') {
                    mode = 0;
                } else {
                    ret = idx % 2 != 0? ret + code.charAt(idx) : ret;
                }
            }
        }
        // */
        
        answer = ret == "" ? "EMPTY" : ret;

        return answer;
    }
}
