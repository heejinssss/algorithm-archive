import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        // int[] answer = {};
        List<Integer> stk = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            // stk이 빈 배열이라면
            if (stk.size() == 0) {
                stk.add(arr[i]);
            // stk에 원소가 있고, stk의 마지막 원소가 arr[i]와 같으면
            } else if (stk.size() >= 1 && stk.get(stk.size()-1) == arr[i]) {
                stk.remove(stk.size()-1);
            // stk에 원소가 있는데 stk의 마지막 원소가 arr[i]와 다르면
            } else if (stk.size() >= 1 && stk.get(stk.size()-1) != arr[i]) {
                stk.add(arr[i]);
            }
        }

        if (stk.size() == 0) stk.add(-1);

        return stk.stream().mapToInt(Integer::intValue).toArray();
    }
}
