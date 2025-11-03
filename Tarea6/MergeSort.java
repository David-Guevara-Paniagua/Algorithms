
public class MergeSort {
    public static int[] mergesort(int data[]) {
        if (data.length > 1) {
            int mitad = data.length / 2;
            int izquierda[] = new int[mitad];
            int derecha[] = new int[data.length - mitad];

            //Dividir el arreglo en izq y der
            int i = 0;
            while (i < mitad) {
                izquierda[i] = data[i];
                i++;
            }

            int j = 0;
            while (i < data.length) {
                derecha[j] = data[i];
                i++;
                j++;
            }

            //Llamada recursiva (hasta que data sea de tamaño 1)
            mergesort(izquierda);
            mergesort(derecha);

            i = 0;
            int d = 0;
            int k = 0;

            //Reorganizar los datos
            while (i < izquierda.length && d < derecha.length) {
                if (izquierda[i] < derecha[d]) {
                    data[k] = izquierda[i];
                    i++;
                } else {
                    data[k] = derecha[d];
                    d++;
                }
                k++;
            }

            //Aniadir los restantes
            while (i < izquierda.length) {
                data[k] = izquierda[i];
                i++;
                k++;
            }
            while (d < derecha.length) {
                data[k] = derecha[d];
                d++;
                k++;
            }
        }
        
        return data;

    }

    public static void main(String args[]) {
        // int info[] = { 38,27,43,3,9,82,10,19,50,61 };
        int info[] = { 3,2,5,4,1 };
        int[] arregloOrdenado=mergesort(info);

        System.out.println();
        System.out.println("Arreglo Ordenado:");
        for (int item:arregloOrdenado){
            System.out.print(item+", ");
        }
        System.out.println();
    }
}