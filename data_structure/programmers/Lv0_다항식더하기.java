class Solution {
    public String solution(String polynomial) {
        int xCount = 0;
        int nCount = 0;

        String[] arr = polynomial.split(" ");

        for (String value : arr) {
            if (value.endsWith("x")) { // x
                xCount += value.startsWith("x") ? 1 : Integer.parseInt(value.substring(0, value.length()-1));
            } else if (!value.equals("+")) { // 상수
                nCount += Integer.parseInt(value);
            }
        }

        String x_str = xCount == 0 ? "" : xCount == 1 ? "x" : xCount + "x";
        String n_str = nCount == 0 ? "" : nCount + "";

        if (xCount == 0) {
            return n_str + "";
        }

        if (nCount == 0) {
            return x_str + "";
        }

        return x_str + " " + "+" + " " + n_str;
    }
}
