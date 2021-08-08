import java.util.*;


class Solution {
    public long solution(long n) {
        long answer = 0;
        
        
        String[] str = String.valueOf(n).split("");
        //System.out.println(Arrays.toString(str));       

        Arrays.sort(str, Collections.reverseOrder());
        //System.out.println(Arrays.toString(str));
        
        String tmp ="";
        for (int i =0; i< str.length; i++){
            tmp += str[i];
            
        }
        
        return Long.parseLong(tmp) ;
        
        
    }
}


// 1차시도 런타임 에러 발생 
import java.util.*;


class Solution {
    public long solution(long n) {
        long answer = 0;
        String[] str = String.valueOf(n).split("");
        //System.out.println(Arrays.toString(str));       

        Arrays.sort(str, Collections.reverseOrder());
        //System.out.println(Arrays.toString(str));
        
      
        String str2 = String.join("", str); 
        answer = Integer.parseInt(str2); 
        // 정해진 타입인 long이 아니라 Int로 변환해서 런타임에러 발생ㅠㅠ;; 자바 
        
        return answer ;
        
        
    }
}
