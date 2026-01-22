import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> arrList = new ArrayList<Integer>();
        List<Integer> delList = Arrays.stream(delete_list).boxed().collect(Collectors.toList());
        
        for (int i = 0; i < arr.length; i++) {
            if (delList.indexOf(arr[i]) == -1) {
                arrList.add(arr[i]);
            }
        }

        return arrList.stream().mapToInt(Integer::intValue).toArray();
    }
}
