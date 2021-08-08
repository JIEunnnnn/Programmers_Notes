import java.util.*;


class Solution {
    public int[] solution(long n) {
        
        String s = String.valueOf(n);
        StringBuilder sb = new StringBuilder(s);
        // stringbuilder은 불변의 객체인 string과 다르게 동적으로 할당가능하다
        
        
        sb = sb.reverse();
        System.out.println(sb); 
        String[] ss = sb.toString().split("");
        System.out.println(Arrays.toString(ss)); 
        
        int[] answer = new int[ss.length];
        for (int i=0; i<ss.length; i++){
            answer[i] = Integer.parseInt(ss[i]);
            // 숫자형의 문자열을, 첫번째 인자값으로 받고, 변환할 진수값을 입력하면
            // 해당 진수에 맞춰 Integer 형 반환
        }
        
        
        return answer ; 
    }
}
