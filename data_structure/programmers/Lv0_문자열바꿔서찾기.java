class Solution {
    public int solution(String myString, String pat) {
        // int answer = 0;
        
        pat = pat.replaceAll("B", "C");
        pat = pat.replaceAll("A", "B");
        pat = pat.replaceAll("C", "A");

        if (myString.contains(pat)) {
            return 1;
        } else {
            return 0;
        }

        // return answer;
    }
}
