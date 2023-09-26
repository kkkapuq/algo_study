import java.io.*;
import java.util.*;

/**
 * 문제 : 추월
 * 링크 : https://www.acmicpc.net/problem/2002
 * 소요시간 :
 */

public class Main {
    static LinkedHashMap<String, Integer> in = new LinkedHashMap<>();
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int answer = 0;

        for (int i = 0; i < N; i++) {
            String car = br.readLine().toString();
            in.put(car, i);
        }

        for (int i = 0; i < N; i++) {
            String outCar = br.readLine().toString();
            Iterator<String> it = in.keySet().iterator();

            while (it.hasNext()) {
                if (in.get(outCar) > in.get(it.next())) {
                    answer++;
                    break;
                }
            }
            
            in.remove(outCar);
        }

        System.out.println(answer);
        br.close();
    }
}
