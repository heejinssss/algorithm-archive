import java.util.*;

class Solution {
    public int solution(String[] spell, String[] dic) {

        Arrays.sort(spell);

        String earth_word = String.join("", spell);

        for (int i = 0; i < dic.length; i++) {
            char[] chars = dic[i].toCharArray(); // 문자열 → 문자 배열
            Arrays.sort(chars);
            String alien_word = new String(chars);

            if (earth_word.equals(alien_word)) {
                return 1;
            }
        }

        return 2;
    }
}
