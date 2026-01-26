import java.util.Arrays;

class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = 0;

        int len1 = arr1.length;
        int len2 = arr2.length;
        int sum1 = Arrays.stream(arr1).sum();
        int sum2 = Arrays.stream(arr2).sum();

        answer = len1 > len2 ? 1 : len1 < len2 ? -1 : sum1 > sum2 ? 1 : sum1 < sum2 ? -1 : 0;

        /*

        // 좌항이 더 크면 1, 작으면 -1, 같으면 0 반환
        Integer.compare(a, b);

        // (절댓값) 좌항이 더 크면 1, 작으면 -1, 같으면 0 반환
        Integer.compareUnsigned(a, b);

        // max, min 값 반환
        Integer.max(a, b); Integer.min(a, b);

        // int 사용 불가
        a.compareTo(b);

        // int 사용 불가
        new Integer(a).equals(b);

        */

        return answer;
    }
}
