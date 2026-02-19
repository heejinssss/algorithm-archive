class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];

        for (int i = 0; i < quiz.length; i++) {
            String[] q_arr = quiz[i].split(" ");

            int X = Integer.parseInt(q_arr[0]);
            int Y = Integer.parseInt(q_arr[2]);
            int Z = Integer.parseInt(q_arr[4]);

            String op = q_arr[1];

            if (op.equals("-")) {
                answer[i] = X - Y == Z ? "O" : "X";
            } else {
                answer[i] =  X + Y == Z ? "O" : "X";
            }

        }

        return answer;
    }
}
