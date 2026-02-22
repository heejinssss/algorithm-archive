class Solution {
    public int solution(String my_string) {
        int answer = 0;
        
        String[] arr = my_string.split(" ");

        answer = Integer.parseInt(arr[0]);

        for (int i = 1; i < arr.length; i++) {
            if (arr[i].equals("+")) {
                answer += Integer.parseInt(arr[i+1]);
            } else if (arr[i].equals("-")) {
                answer -= Integer.parseInt(arr[i+1]);
            } else {
                continue;
            }
        }
        return answer;
    }
}
