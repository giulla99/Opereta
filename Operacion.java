package Opermat;
import java.util.*;

/**
 * Created by Giullianodam on 19/6/17.
 */
public class Operacion {
    public int[][] Operador(Hashtable<String, int [][]> mat, String operando, String operador, String operando2){
        int[][] matriz1= mat.get(operando);
        int[][] matriz2 = mat.get(operando2);
        int[][] r = new int[matriz1.length][matriz1[0].length];
        for (int x=0;x<matriz1.length;x++){
            for (int y=0;y<matriz1[0].length;y++){
                if (operador.equals("+")){
                    r[x][y] = matriz1[x][y] + matriz2[x][y];
                }
                if (operador.equals("-")){
                    r[x][y] = matriz1[x][y] - matriz2[x][y];
                }
                if (operador.equals("*")){
                    r[x][y] = matriz1[x][y] * matriz2[x][y];
                }
            }
        }
        return r;
    }
}
