class Solution {
    public int solution(String binomial) {
        int answer = 0;

        String[] strList = binomial.split(" ");

        /*
        String a    = "";
        String b    = "";
        String op   = "";

        for (String str : strList) {
            if ("+-*".contains(str)) {
                op = str;
            } else {
                a = a.equals("") ? str  : a;
                b = a.equals("") ? ""   : str;
            }
        }
        */
        
        switch(strList[1]) {
            case "+":
                answer = Integer.parseInt(strList[0]) + Integer.parseInt(strList[2]);
                break;
            case "-":
                answer = Integer.parseInt(strList[0]) - Integer.parseInt(strList[2]);
                break;
            case "*":
                answer = Integer.parseInt(strList[0]) * Integer.parseInt(strList[2]);
                break;
            default:
                break;
        }
        
        return answer;
    }
}
