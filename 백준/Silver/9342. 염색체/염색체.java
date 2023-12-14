
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int t;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t= Integer.parseInt(br.readLine());
        for(int i=0; i<t; i++){
            String s = br.readLine();
            boolean check =false;
            int a= s.indexOf("A");
            int f= s.indexOf("F");
            int c = s.indexOf("C");
            int aLast= s.lastIndexOf("A");
            int fLast= s.lastIndexOf("F");
            if(s.charAt(s.length()-1)=='A' ||s.charAt(s.length()-1)=='F'||s.charAt(s.length()-1)=='C'){
                if(a<f && f<c){
                    if(aLast==f-1 && fLast==c-1){
                        check=true;
                    }
                }
            }
            if(check){
                System.out.println("Infected!");
            }
            else{
                System.out.println("Good");
            }
        }
    }
}
