package Opermat;

import java.util.*;
/**
 * Created by Giullianodam on 19/6/17.
 */
public class Precedencia {
    public void InfPost(String datos,  Hashtable<String, int[][]> mat){
        String expr = depurar(datos);
        String[] arrayInfix = expr.split(" ");
        //Declaración de las pilas
        Stack < String > E = new Stack <  > (); //Pila entrada
        Stack < String > P = new Stack <  > (); //Pila temporal para operadores
        Stack < String > S = new Stack <  > (); //Pila salida

        //Añadir la array a la Pila de entrada (E)
        for (int i = arrayInfix.length - 1; i >= 0; i--) {
            E.push(arrayInfix[i]);
        }

        try {
            //Algoritmo Infijo a Postfijo
            while (!E.isEmpty()) {
                switch (pref(E.peek())){
                    case 1:
                        P.push(E.pop());
                        break;
                    case 3:
                    case 4:
                        while(pref(P.peek()) >= pref(E.peek())) {
                            S.push(P.pop());
                        }
                        P.push(E.pop());
                        break;
                    case 2:
                        while(!P.peek().equals("(")) {
                            S.push(P.pop());
                        }
                        P.pop();
                        E.pop();
                        break;
                    default:
                        S.push(E.pop());
                }
            }

            //Eliminacion de `impurezas´ en la expresiones algebraicas
            //String infix = expr.replace(" ", "");
            //String postfix = S.toString().replaceAll("[\\]\\[,]", "");
            //System.out.println(postfix);
            //Mostrar resultados
            //char[] postfija = postfix.toCharArray();
            int tama = 0;
            int[][] result;
            while (S.size()>1){
                if (mat.get(S.get(tama)) == null){
                    Operacion miop;
                    miop = new Operacion();
                    result = miop.Operador(mat, S.get(tama-2), S.get(tama) , S.get(tama-1));
                    mat.put("resultado", result);
                    S.remove(tama);
                    S.remove(tama-1);
                    S.remove(tama-2);
                    S.add(tama-2, "resultado");
                    tama = tama-2;
                }
                tama++;
            }
            int[][] matriz_final;
            matriz_final = mat.get(S.get(0));
            for (int t=0;t<matriz_final.length;t++){
                for (int t2=0;t2<matriz_final[0].length;t2++){
                    if (t2==0){
                        System.out.println();
                    }
                    System.out.print(matriz_final[t][t2]+" ");
                }
            }
            //ArrayList<String> postfinal;
            //postfinal=new ArrayList<>();
            //int i;
            //for (i=0;i<postfija.length;i++){
                //char nuevo = postfija[i];
                //String str = Character.toString(nuevo);
                //postfinal.add(str);
            //}
            //P4 miMatriz;
            //miMatriz=new P4();
            //System.out.println(postfinal);
            //miMatriz.expresionAlgebraica(postfinal, dic,dicaux);
        }
        catch(Exception ex){
            System.out.println("Error en la expresión algebraica");
            System.err.println(ex);
        }
    }

    //Depurar expresión algebraica
    private static String depurar(String s) {
        s = s.replaceAll("\\s+", ""); //Elimina espacios en blanco
        s = "(" + s + ")";
        String simbols = "+-*/()";
        String str = "";
        //Deja espacios entre operadores
        for (int i = 0; i < s.length(); i++) {
            if (simbols.contains("" + s.charAt(i))) {
                str += " " + s.charAt(i) + " ";
            }else str += s.charAt(i);
        }
        return str.replaceAll("\\s+", " ").trim();
    }

    //Jerarquia de los operadores
    private static int pref(String op) {
        int prf = 99;
        if (op.equals("^")) prf = 5;
        if (op.equals("*")) prf = 4;
        if (op.equals("+") || op.equals("-")) prf = 3;
        if (op.equals(")")) prf = 2;
        if (op.equals("(")) prf = 1;
        return prf;
    }
}
