import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class solution {
    public static void main(String[] args) {
        Scanner stdin=new Scanner(System.in);
        int n=stdin.nextInt();
        int k=stdin.nextInt();
        int prices[]=new int[n];
        for(int i=0;i<n;i++) prices[i]=stdin.nextInt();
        Arrays.sort(prices);
        int answer = 0;
        for(int i=0;i<n;i++){
          if (prices[i]>k) {
            break;
          }
          k = k-prices[i];
          answer++;
        }
        System.out.println(answer);
    }
}
