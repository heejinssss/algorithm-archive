import java.util.Arrays;

class Solution {
    public String[] solution(String my_string) {
	int str_len = my_string.length();
	String[] answer = new String[str_len];
	
	for (int i = str_len; i > 0; i--) {
		answer[i-1] = my_string.substring(i-1);
	}

    Arrays.sort(answer);

    return answer;
    }
}
