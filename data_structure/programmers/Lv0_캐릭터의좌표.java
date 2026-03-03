import java.util.*;

class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int pi = board[0] / 2;
        int pj = board[1] / 2;

        Map<String, int[]> dirs = new HashMap<>();

        dirs.put("left",  new int[]{-1,  0});
        dirs.put("right", new int[]{ 1,  0});
        dirs.put("up",    new int[]{ 0,  1});
        dirs.put("down",  new int[]{ 0, -1});

        int ci = 0, cj = 0;

        for (String key : keyinput) {
            int[] dir = dirs.get(key); // ex. [ -1, 0 ]

            int ni = ci + dir[0];
            int nj = cj + dir[1];

            // 보드 밖이면 무시
            if (ni < -pi || ni > pi || nj < -pj || nj > pj) continue;

            ci = ni;
            cj = nj;
        }

        return new int[]{ci, cj};
    }
}
