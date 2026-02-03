class Solution {
    public String solution(String my_string, int[] indices) {
        String answer = "";

        for (int indice : indices) {
            my_string = my_string.substring(0, indice) + "$" + my_string.substring(indice + 1);
        }

        answer = my_string.replace("$", "");

        return answer;
    }
}
