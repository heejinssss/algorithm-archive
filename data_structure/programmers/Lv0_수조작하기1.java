class Solution {
    public int solution(int n, String control) {
        int answer = 0;
        
        int w = (int) countChar(control, 'w');
        int a = (int) countChar(control, 'a');
        int s = (int) countChar(control, 's');
        int d = (int) countChar(control, 'd');
        
        answer = n + (w * 1) + (s * (-1)) + (d * 10) + (a * (-10));
    
        return answer;
    }
    
    public static long countChar(String str, char ch) {
        return str.chars()
            .filter(c -> c == ch)
            .count();
    }
}
