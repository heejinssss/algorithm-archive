class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        int s = 0;
        int e = 0;
        int k = 0;
        
        for (int[] query : queries) {
            s = query[0];
            e = query[1];

            for (int i = s; i <= e; i++) {
                arr[i] += + 1;
            }
        }

        answer = arr;

        return answer;
    }
}
