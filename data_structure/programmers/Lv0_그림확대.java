import java.util.*;

class Solution {
    public String[] solution(String[] picture, int k) {

        List<String> answer = new ArrayList<>();
        
        for (int i = 0; i < picture.length; i++) {
            for (int ck = 0; ck < k; ck++) { //==== 열 반복용
                String temp = "";
                for (int j = 0; j < picture[i].length(); j++) {
                    String temp_part = "";
                    for (int cr = 0; cr < k; cr++) { //==== 행 반복용
                        temp_part += picture[i].substring(j, j+1);
                    }
                    temp += temp_part;
                }
                answer.add(temp);
            }
        }
        return answer.toArray(new String[0]);
    }
}
