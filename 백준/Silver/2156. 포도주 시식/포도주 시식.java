import java.io.*;
import java.util.*;

public class Main {

    static int bottles;
    static Integer[] amounts;
    static Integer[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        bottles = Integer.parseInt(bf.readLine());

        amounts = new Integer[bottles+1];

        for(int i = 1; i < bottles+1; i++) {
            amounts[i] = Integer.parseInt(bf.readLine());
        }

        dp = new Integer[bottles+1];

        dp[0] = 0;
        dp[1] = amounts[1];
        if(bottles>1)
            dp[2] = amounts[1]+amounts[2];

        for(int i = 3; i < dp.length; i++) {
            dp[i] = Math.max(Math.max(dp[i-2]+amounts[i], dp[i-1]), dp[i-3]+amounts[i-1]+amounts[i]);
        }
        System.out.println(dp[bottles]);
    }

}
