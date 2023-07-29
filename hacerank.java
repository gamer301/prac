import java.util.Scanner;
public class hacerank {

    public static void main(String[] args) 
{
        Scanner scr = new Scanner(System.in);
        int t =0;
        t =  scr.nextInt();
        int flag = 0;
        for (int i=0; i<=t;i++)
    {          
        int n = 0;
            n=  scr.nextInt();
        int s[]=new int [n];
        int t1[]=new int [n];
        for (int j=0; j<=n;j++)
        {
           s[j]=scr.nextInt(); 
        }
        for (int l=0; l<=n;l++)
        {
           t1[l]=scr.nextInt(); 
        }
        scr.close(); 
         for (int p=0; p<=n;p++)
        {
             
           for (int u=0; u<=n;u++)
         {
           if (s[p]==t1[u])
           {
               flag += 1;
               break;
           }
           else 
           {
               break;
           }
         } 
        }   
    if (flag==n)
               {
                   System.out.print("true");
                   
               }
               else
               {
                   System.out.print("false");
               }
        
        
            }

     }
}