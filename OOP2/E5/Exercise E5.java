//Exercício E5- POO II

import java.lang.reflect.Field;
import java.util.Scanner;

public class Sandy {
    private String atributo1;
    private int atributo2;
    private boolean atributo3;

    public void listarAtributos() {
        Field[] campos = this.getClass().getDeclaredFields();

        System.out.println("Atributos disponíveis:");

        for (Field campo : campos) {
            System.out.println(campo.getName());
        }
    }

    public void valorarAtributo(String atributo) {
        try {
            Field campo = this.getClass().getDeclaredField(atributo);
            Class<?> tipo = campo.getType();
            Scanner scanner = new Scanner(System.in);

            System.out.println("Digite o valor para o atributo " + atributo + " (tipo: " + tipo.getSimpleName() + "):");
            if (tipo == String.class) {
                String valor = scanner.nextLine();
                campo.set(this, valor);
            } else if (tipo == int.class) {
                int valor = scanner.nextInt();
                campo.setInt(this, valor);
            } else if (tipo == boolean.class) {
                boolean valor = scanner.nextBoolean();
                campo.setBoolean(this, valor);
            }

            System.out.println("Atributo " + atributo + " valorado com sucesso!");
        } catch (NoSuchFieldException | IllegalAccessException e) {
            System.out.println("Erro ao valorar atributo: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        Sandy sandy = new Sandy();

        sandy.listarAtributos();

        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o nome do atributo que deseja valorar:");
        String atributo = scanner.nextLine();

        sandy.valorarAtributo(atributo);
    }
}

//Essas modificações permitem que o usuário tenha uma visão dos atributos disponíveis antes de tomar a decisão de qual atributo valorar.
