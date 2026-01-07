class Solution {
    public String solution(String n_str) {
        String answer = "";
        
        int index = 0;
        boolean isThereZeroStr = false;

        for (int i = 0; i < n_str.length()-1; i++) {
            if ("0".equals(n_str.substring(i, i+1))) {
                isThereZeroStr = true;
                continue;
            } else {
                index = i;
                break;
            }
        }
        
        if (index == 0 && isThereZeroStr) {
            answer = n_str.substring(n_str.length()-1);
        } else {
            answer = n_str.substring(index);   
        }
    
        return answer;
    }
}
