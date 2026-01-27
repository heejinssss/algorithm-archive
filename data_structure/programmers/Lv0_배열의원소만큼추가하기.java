import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        /*
        List<Integer> answer = new ArrayList<>();

        for (int a : arr) {
            int idx = a;
            while (idx > 0) {
                answer.add(a);
                idx--;
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
        */

        // 1. 결과 배열 크기 계산
        int size = 0;
        for (int a : arr) { size += a; }

        // 2. 정확한 크기의 배열 생성
        int[] answer = new int[size];

        // 3. 값 채우기
        int index = 0;
        for (int a : arr) {
            for (int i = 0; i < a; i++) {
                answer[index++] = a;
            }
        }

        return answer;
    }
}
