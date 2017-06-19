package Opermat;

import java.io.IOException;
import java.util.*;
import java.io.File;
import java.awt.Desktop;

public class P4 {

    public static Hashtable<String, int[][]> mat = new Hashtable<>();

    public static void main(String[] args) throws IOException{
        // write your code here
        int valores[][];
        while (true) {
            System.out.println("\nIngrese el comando");
            Scanner entrada = new Scanner(System.in);
            String comando = entrada.nextLine();
            comando = comando.toLowerCase();
            String[] accion = comando.split(" ");
            if (accion[0].equals("fin") || accion[0].equals("finalizar")) {
                System.out.println("Gracias por usar Opermat, hasta luego");
                System.exit(0);
            }
            if (accion[0].equals("ayu") || accion[0].equals("ayuda")) {
                if (Desktop.isDesktopSupported()){
                        File myFile = new File("/Users/Giullianodam/Desktop/Manual.pdf");
                        Desktop.getDesktop().open(myFile);
                }
                continue;
            }
            if (accion[0].equals("lee") || accion[0].equals("leer")){
                Scanner lector = new Scanner(System.in);
                System.out.println("Cantidad de filas");
                int filas = lector.nextInt();
                System.out.println("Cantidad de columnas");
                int columnas = lector.nextInt();
                int matriz[][] = new int [filas][columnas];
                for (int f=0;f<filas;f++){
                    for (int c=0;c<columnas;c++) {
                        System.out.println("Ingrese el numero para la fila " + f + " y columna " + c);
                        matriz[f][c] = lector.nextInt();

                    }}
                    mat.put(accion[1], matriz);
                int[][] mat_imp=mat.get(accion[1]);
                for (int x=0;x<mat.get(accion[1]).length;x++){
                    for (int y=0;y<mat.get(accion[1])[0].length;y++){
                        if (y==0){
                            System.out.println("");
                        }
                        System.out.print(mat_imp[x][y]+" ");
                    }
                }
                continue;
            }
            if (mat.get(accion[0])!=null && accion.length<2) {
                int[][] mat_g = mat.get(accion[0]);
                for (int x = 0; x < mat.get(accion[0]).length; x++) {
                    for (int y = 0; y < mat.get(accion[0])[0].length; y++) {
                        if (y == 0) {
                            System.out.println("");
                        }
                        System.out.print(mat_g[x][y] + " ");
                    }
                }
                continue;
            }
            if (accion[0].equals("mae") || accion[0].equals("matrizaleatoriaenteros")){
                Scanner enteros = new Scanner(System.in);
                System.out.println("Cantidad de filas");
                int filas = enteros.nextInt();
                System.out.println("Cantidad de columnas");
                int columnas = enteros.nextInt();
                int matriz_e[][] = new int [filas][columnas];
                for (int f=0;f<filas;f++) {
                    for (int c = 0; c < columnas; c++) {
                        Random randint = new Random();
                        int x = randint.nextInt(100);
                        matriz_e[f][c] = x;
                        if (c==0){
                            System.out.println("");
                        }
                        System.out.print(matriz_e[f][c]+" ");
                    }
                }
                mat.put(accion[1],matriz_e);
            }
            if (accion[1].equals("+") && 4>accion.length) {
                for (int y = 0; y < accion.length; y++) {
                    System.out.print(accion[y] + " ");
                }
                int[][] matriz1 = mat.get(accion[0]);
                int[][] matriz2 = mat.get(accion[2]);
                int[][] result = new int[matriz1.length][matriz1[0].length];
                for (int f = 0; f < matriz1.length; f++) {
                    for (int c = 0; c < matriz1[0].length; c++) {
                        result[f][c] = matriz1[f][c] + matriz2[f][c];
                        if (c == 0) {
                            System.out.println("");
                        }
                        System.out.print(result[f][c] + " ");
                    }
                }
            }
            if (accion[1].equals("-") && 4>accion.length) {
                for (int y = 0; y < accion.length; y++) {
                    System.out.print(accion[y] + " ");
                }
                int[][] matriz1 = mat.get(accion[0]);
                int[][] matriz2 = mat.get(accion[2]);
                int[][] result = new int[matriz1.length][matriz1[0].length];
                for (int f = 0; f < matriz1.length; f++) {
                    for (int c = 0; c < matriz1[0].length; c++) {
                        result[f][c] = matriz1[f][c] - matriz2[f][c];
                        if (c == 0) {
                            System.out.println("");
                        }
                        System.out.print(result[f][c] + " ");
                    }
                }
            }
            if (accion[1].equals("*") && 4>accion.length) {
                for (int y = 0; y < accion.length; y++) {
                    System.out.print(accion[y] + " ");
                }
                int[][] matriz1 = mat.get(accion[0]);
                int[][] matriz2 = mat.get(accion[2]);
                int[][] result = new int[matriz1.length][matriz1[0].length];
                for (int f = 0; f < matriz1.length; f++) {
                    for (int c = 0; c < matriz1[0].length; c++) {
                        result[f][c] = matriz1[f][c] * matriz2[f][c];
                        if (c == 0) {
                            System.out.println("");
                        }
                        System.out.print(result[f][c] + " ");
                    }
                }
            }
            if (accion[1].equals("**") && 4>accion.length) {
                for (int y = 0; y < accion.length; y++) {
                    System.out.print(accion[y] + " ");
                }
                int pow = Integer.parseInt(accion[2]);
                int[][] matriz1 = mat.get(accion[0]);
                int[][] result = new int[matriz1.length][matriz1[0].length];
                for (int f = 0; f < matriz1.length; f++) {
                    for (int c = 0; c < matriz1[0].length; c++) {
                        result[f][c] = (int) Math.pow(matriz1[f][c],pow);
                        if (c == 0) {
                            System.out.println("");
                        }
                        System.out.print(result[f][c] + " ");
                    }
                }
            }
            if (accion[1].equals("=") && accion.length<6){
                if (accion[3].equals("+")) {
                    for (int y = 0; y < accion.length; y++) {
                        System.out.print(accion[y] + " ");
                    }
                    int[][] matriz1 = mat.get(accion[2]);
                    int[][] matriz2 = mat.get(accion[4]);
                    int[][] result = new int[matriz1.length][matriz1[0].length];
                    for (int f = 0; f < matriz1.length; f++) {
                        for (int c = 0; c < matriz1[0].length; c++) {
                            result[f][c] = matriz1[f][c] + matriz2[f][c];
                            if (c == 0) {
                                System.out.println("");
                            }
                            System.out.print(result[f][c] + " ");
                        }
                    }
                    mat.put(accion[0],result);
                }
                    if (accion[3].equals("-")) {
                        for (int y = 0; y < accion.length; y++) {
                            System.out.print(accion[y] + " ");
                        }
                        int[][] matriz3 = mat.get(accion[2]);
                        int[][] matriz4 = mat.get(accion[4]);
                        int[][] result1 = new int[matriz3.length][matriz3[0].length];
                        for (int f = 0; f < matriz3.length; f++) {
                            for (int c = 0; c < matriz3[0].length; c++) {
                                result1[f][c] = matriz3[f][c] - matriz4[f][c];
                                if (c == 0) {
                                    System.out.println("");
                                }
                                System.out.print(result1[f][c] + " ");
                            }
                        }
                        mat.put(accion[0],result1);
                    }
                    if (accion[3].equals("*")) {
                        for (int y = 0; y < accion.length; y++) {
                            System.out.print(accion[y] + " ");
                        }
                        int[][] matriz5 = mat.get(accion[2]);
                        int[][] matriz6 = mat.get(accion[4]);
                        int[][] result2 = new int[matriz5.length][matriz5[0].length];
                        for (int f = 0; f < matriz5.length; f++) {
                            for (int c = 0; c < matriz5[0].length; c++) {
                                result2[f][c] = matriz5[f][c] * matriz6[f][c];
                                if (c == 0) {
                                    System.out.println("");
                                }
                                System.out.print(result2[f][c] + " ");
                            }
                        }
                        mat.put(accion[0],result2);
                    }
                    if (accion[3].equals("**")) {
                        for (int y = 0; y < accion.length; y++) {
                            System.out.print(accion[y] + " ");
                        }
                        int[][] matriz7 = mat.get(accion[2]);
                        int pow = Integer.parseInt(accion[4]);
                        int[][] result3 = new int[matriz7.length][matriz7[0].length];
                        for (int f = 0; f < matriz7.length; f++) {
                            for (int c = 0; c < matriz7[0].length; c++) {
                                result3[f][c] = (int) Math.pow(matriz7[f][c], pow);
                                if (c == 0) {
                                    System.out.println("");
                                }
                                System.out.print(result3[f][c] + " ");
                            }
                        }
                        mat.put(accion[0],result3);
                    }

                }
            }
        }
    }
