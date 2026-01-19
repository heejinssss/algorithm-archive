import java.lang.Math;
import java.util.Arrays;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;

        int[] arr = {a,b,c,d};

        // a~d를 낮은수부터 정렬
        Arrays.sort(arr);
        a = arr[0]; b = arr[1]; c = arr[2]; d = arr[3];
        
        //==== 1
        if (a == d) {
            answer = 1111*a;
        //==== 2
        } else if (a == c && a != d) {
            answer = (int) Math.pow((10*a+d), 2);
        } else if (b == d && a != b) {
            answer = (int) Math.pow((10*b+a), 2);
        //==== 3
        } else if (a == b && c == d && a != c) {
            answer = ((a+c)*(c-a));
        //==== 4
        } else if (a == b && a != c && a != d && c != d) {
            answer = c*d;
        } else if (b == c && a != b && b != d && a != d) {
            answer = a*d;
        } else if (c == d && a != c && b != c && a != b) {
            answer = a*b;
        //==== 5
        } else {
            answer = a;
        }
        return answer;
    }
}
