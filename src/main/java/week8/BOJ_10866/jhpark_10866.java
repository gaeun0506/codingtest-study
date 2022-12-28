package main.java.week8.BOJ_10866;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class jhpark_10866 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        Deque<String> deque = new ArrayDeque<>();

        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            String s = st.nextToken();

            switch(s) {
                case "push_front":
                    deque.addFirst(st.nextToken());
                    break;

                case "push_back":
                    deque.addLast(st.nextToken());
                    break;

                case "pop_front":
                    if(deque.isEmpty()) {
                        sb.append(-1).append("\n");
                    } else {
                        sb.append(deque.poll()).append("\n");
                    }
                    break;

                case "pop_back":
                    if(deque.isEmpty()) {
                        sb.append(-1).append("\n");
                    } else {
                        sb.append(deque.pollLast()).append("\n");
                    }
                    break;

                case "size":
                    sb.append(deque.size()).append("\n");
                    break;

                case "empty":
                    if(deque.isEmpty()) {
                        sb.append(1).append("\n");
                    } else {
                        sb.append(0).append("\n");
                    }
                    break;

                case "front":
                    if(deque.isEmpty()) {
                        sb.append(-1).append("\n");
                    } else {
                        sb.append(deque.peekFirst()).append("\n");
                    }
                    break;

                case "back":
                    if(deque.isEmpty()) {
                        sb.append(-1).append("\n");
                    } else {
                        sb.append(deque.peekLast()).append("\n");
                    }
                    break;
            }
        }

        System.out.println(sb);
    }
}
