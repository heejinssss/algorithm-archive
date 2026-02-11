import java.util.ArrayList;

class Solution {
    public String[] solution(String my_string) {
        // /*
        String[] arr = my_string.split(" ");
        ArrayList<String> answer = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            if (!arr[i].equals("")) answer.add(arr[i]);
        }
        
        return answer.toArray(new String[0]);
        // */
        
        // 1
        // return my_string.trim().split("[ ]+");

        // 2
        return my_string.trim().split("\\s+");
    }
}
