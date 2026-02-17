class Solution {
    public int solution(int[][] dots) {
        int answer = 0;

        int[][] idx = new int[][]{
            new int[]{ 0, 1, 2, 3 },
            new int[]{ 0, 2, 1, 3 },
            new int[]{ 0, 3, 1, 2 }
        };

        for (int i = 0; i < 3; i++) {
            double x1 = dots[idx[i][0]][0];
            double x2 = dots[idx[i][1]][0];
            double x3 = dots[idx[i][2]][0];
            double x4 = dots[idx[i][3]][0];

            double y1 = dots[idx[i][0]][1];
            double y2 = dots[idx[i][1]][1];
            double y3 = dots[idx[i][2]][1];
            double y4 = dots[idx[i][3]][1];

            if (Math.abs((y2-y1)/(x2-x1)) == Math.abs((y4-y3)/(x4-x3))) {
                return 1;
            }
        }

        return answer;
    }
}
