class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};

        int i = 0;
        int j = 0;
        int arri = 0;
        int arrj = 0;

        for (int idx = 0; idx < queries.length; idx++) {
            i = queries[idx][0];
            j = queries[idx][1];

            arri = arr[i]; // arr의 i번째 인덱스 값
            arrj = arr[j]; // arr의 j번째 인덱스 값

            arr[i] = arrj; // arr의 i번째 인덱스 값을, j번째 인덱스 값으로 변경
            arr[j] = arri; // arr의 j번째 인덱스 값을, i번째 인덱스 값으로 변경
        }

        answer = arr;

        return answer;
    }
}
