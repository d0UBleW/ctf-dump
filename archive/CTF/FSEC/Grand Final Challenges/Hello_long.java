import java.io.PrintStream;
import java.util.Scanner;

public class Hello_long {

    public Hello_long() {}

    public static Boolean securing_fsecure(String paramString) {
        boolean bool = false;
        if (42L + -37L * Long.parseLong(paramString) == 17206538690L) {
          bool = true;
          getHexString(paramString);
          System.out.println("\nYay! I think I got it!? The flag is here somewhere...");
        }
        return Boolean.valueOf(bool);
    }

    public static void getHexString(String paramString) {
        String str = hexToASCII("" + paramString.charAt(10) + paramString.charAt(19) + paramString.charAt(4) + paramString.charAt(12) + paramString.charAt(6) + paramString.charAt(8) + paramString.charAt(1) + paramString.charAt(16) + paramString.charAt(2) + "c" + paramString.charAt(6) + "f" + paramString.charAt(1) + "e" + paramString.charAt(2) + paramString.charAt(4) + paramString.charAt(19) + paramString.charAt(12) + paramString.charAt(4) + paramString.charAt(16) + paramString.charAt(10) + paramString.charAt(15) + paramString.charAt(19) + paramString.charAt(7) + paramString.charAt(4) + paramString.charAt(11));
    }

    public static String hexToASCII(String paramString) {
        StringBuilder localStringBuilder = new StringBuilder("");
        for (int i = 0; i < paramString.length(); i += 2) {
          localStringBuilder.append((char)Integer.parseInt(paramString.substring(i, i + 2), 16));
        }
        return localStringBuilder.toString();
    }

    public static void creator(Integer[] paramArrayOfInteger) {
      int i = 0;

      StringBuilder localStringBuilder = new StringBuilder();
      int j = paramArrayOfInteger.length;
      while (i < j)
      {
        localStringBuilder.append(paramArrayOfInteger[i].intValue());
        i++;
      }

      String str = hexToASCII(localStringBuilder.toString());
      System.out.println("Author: " + str);
    }

    public static void main(String[] paramArrayOfString) throws Exception {
        String[] arrayOfString = new String[28];
        arrayOfString[0] = "two plus two";
        arrayOfString[1] = "one minus one";
        arrayOfString[2] = "six minus two";
        arrayOfString[3] = "two plus four";
        arrayOfString[4] = "two plus three";
        arrayOfString[5] = "two plus one";
        arrayOfString[6] = "three plus three";
        arrayOfString[7] = "ten minus five";
        arrayOfString[8] = "negative one plus seven";
        arrayOfString[9] = "three plus zero";
        arrayOfString[10] = "two plus five";
        arrayOfString[11] = "three plus two";
        arrayOfString[12] = "four plus three";
        arrayOfString[13] = "five minus three";
        arrayOfString[14] = "negative three plus nine";
        arrayOfString[15] = "three plus two";
        arrayOfString[16] = "nine minus five";
        arrayOfString[17] = "one plus two";
        arrayOfString[18] = "four plus three";
        arrayOfString[19] = "eleven minus two";
        arrayOfString[20] = "three plus three";
        arrayOfString[21] = "minus five plus seven";
        arrayOfString[22] = "six plus zero";
        arrayOfString[23] = "three plus two";
        arrayOfString[24] = "four plus three";
        arrayOfString[25] = "zero plus two";
        arrayOfString[26] = "four plus three";
        arrayOfString[27] = "negative three plus five";

        Integer[] arrayOfInteger = new Integer[28];
        Scanner localScanner = new Scanner(System.in);
        for (int i = 0; i < arrayOfString.length; i++) {
          System.out.println(" " + arrayOfString[i] + " ");
          arrayOfInteger[i] = Integer.valueOf(localScanner.nextInt());
        }

        creator(arrayOfInteger);
        if (securing_fsecure("7265706c61633374683173").booleanValue() == true) {
          System.out.println("You got it! Good job!!!");
        }
        else
        {
          System.out.println("You're good with numbers for sure. :P");
        }
    }
}
