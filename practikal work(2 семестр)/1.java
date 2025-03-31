class Main {
    public static boolean checkEnding(String str1, String str2) {
        if (str2.length() > str1.length()) {
            return false;
        }

        String endOfStr1 = str1.substring(str1.length() - str2.length());

        return endOfStr1.equals(str2);
    }
}

