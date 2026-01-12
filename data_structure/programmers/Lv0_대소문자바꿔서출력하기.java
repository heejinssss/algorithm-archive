import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();

        String answer = "";
        char pivot;
        
        for (int i = 0; i < a.length(); i++) {
            pivot = a.charAt(i);
            if (Character.isUpperCase(pivot)) {
                answer += Character.toLowerCase(pivot);
            } else {
                answer += Character.toUpperCase(pivot);          
            }
        }
        
        System.out.print(answer);
    }
}
