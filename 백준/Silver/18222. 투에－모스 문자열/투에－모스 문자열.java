import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long k = Long.parseLong(br.readLine());

        int answer = recursive(k-1);
        System.out.println(answer);
    }

    private static int recursive(long k) {
        if(k == 0)
            return 0;
        else if(k == 1)
            return 1;
        else if(k % 2 == 0)
            return recursive(k/2);
        else
            return 1 - recursive(k/2);
    }
}