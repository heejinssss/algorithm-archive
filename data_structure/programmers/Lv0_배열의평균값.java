class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int count = numbers.length;
        int temp = 0;

        for (int number : numbers) {
            temp += number;
        }
        
        answer = (double) temp / count;

        return answer;
    }
}
