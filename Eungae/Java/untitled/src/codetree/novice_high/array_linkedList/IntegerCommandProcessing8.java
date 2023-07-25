package codetree.novice_high.array_linkedList;

import java.util.*;

public class IntegerCommandProcessing8 {
    public void solution() {
        LinkedList list = new LinkedList<Integer>();
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for(int i = 0; i < n; i++){
            String order = sc.next();
            if(order.equals("push_front")){
                int num = sc.nextInt();
                list.addFirst(num);
            } else if(order.equals("push_back")){
                int num = sc.nextInt();
                list.addLast(num);
            } else if(order.equals("pop_front")){
                System.out.println(list.pollFirst());
            } else if(order.equals("pop_back")){
                System.out.println(list.pollLast());
            } else if(order.equals("size")){
                System.out.println(list.size());
            } else if(order.equals("empty")){
                System.out.println(list.isEmpty() ? 1 : 0);
            } else if(order.equals("front")){
                System.out.println(list.peekFirst());
            } else {
                System.out.println(list.peekLast());
            }
        }

    }
}
