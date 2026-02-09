import java.util.ArrayList;

class Solution {
    public int[] solution(String myString) {
        // int[] answer = {};
        ArrayList<Integer> answer = new ArrayList<>();

        String[] strs = myString.split("x");

        for (String str : strs) {
            answer.add(str.length());
        }

        if (myString.endsWith("x")) {
            answer.add(0);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();

        /*
        return Arrays.stream(myString.split("x", myString.length()))
            .mapToInt(x -> x.length())
            .toArray();
        */
    }
}
