class Solution {
    public int[][] solution(int n) {
        int[][] arr = new int[n][n];

        int si = 0, sj = 0, ni = 0, nj = 0, num = 1;
        arr[si][sj] = num++;

        int[] di = new int[]{ 0, 1, 0, -1 };
        int[] dj = new int[]{ 1, 0, -1, 0 };

        while (num <= n * n) {
            for (int x = 0; x < 4; x++) {
                while (true) {
                    if (0 <= si + di[x] && si + di[x] < n && 0 <= sj + dj[x] && sj + dj[x] < n && arr[si + di[x]][sj + dj[x]] == 0) {
                        arr[si + di[x]][sj + dj[x]] = num;
                        num++;
                        si += di[x];
                        sj += dj[x];
                    } else {
                        break;
                    }
                }
            }
        }

        return arr;
    }
}
