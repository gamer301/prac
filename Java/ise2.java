public class ise2{
public static void main(String args[])
    {
        // Given string str
        String txt = "GeeksForGeeks";
        String pat = "ee";

        int m = pat.length();
        int n = txt.length();
        int i=0;        
        for (i = 0;i<=n-m; i++) 
      {   
        if (pat.equals(txt.substring(i,i+m)))
        {
            System.out.println("Pattern found at index "+ i);
        }
      }    
    }
}

