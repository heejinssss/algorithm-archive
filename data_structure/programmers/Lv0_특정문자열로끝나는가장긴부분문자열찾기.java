class Solution {
    public String solution(String myString, String pat) {
        String answer = "";

        int index = 0;

        /*
        for (int i = 0; i < myString.length(); i++) {
            if (myString.substring(i).startsWith(pat)) {
                index = i;
            }
        }
        */
        
        index = myString.lastIndexOf(pat);

        answer = myString.substring(0,index) + pat;

        return answer;
    }
}
