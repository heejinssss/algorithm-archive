import java.util.Arrays;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int[] answer = {};
        int a = slicer[0];
        int b = slicer[1];
        int c = slicer[2];
        // num_list = [a, b, c];

        switch (n) {
            case 1:
                // 0~b
                answer = Arrays.copyOfRange(num_list, 0, b+1);
                break;
            case 2:
                // a~
                answer = Arrays.copyOfRange(num_list, a, num_list.length);
                break;
            case 3:
                // a~b
                answer = Arrays.copyOfRange(num_list, a, b+1);
                break;
            case 4:
                // a~b (간격 c)
                int idx = 0;
                int[] temp = new int[((b-a)/c)+1];
                while (a+(c*idx) <= b) {
                    temp[idx] = num_list[a+(c*idx)];
                    idx++;
                }
                answer = temp;
                break;
            default:
                break;
        }

        return answer;
    }
}
