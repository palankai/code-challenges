package palankai.io;

import java.util.Hashtable;
import java.util.function.Consumer;

public class DiagnosticReport implements Consumer<String> {
    Hashtable<Integer, Integer> ones;
    DiagnosticReport() {
        ones = new Hashtable<>();
    }

    @Override
    public void accept(String s) {
        System.out.println(s);
        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) == '1') {
                this.foundOne(i);
            } else if(s.charAt(i) == '0') {
                this.foundZero(i);
            }
        }
    }

    public void summarise() {
        String gamma = "";
        String epsilon = "";
        for(Integer i=0; i<ones.size();i++) {
            if(ones.get(i) > 0) {
                gamma = gamma.concat("1");
                epsilon = epsilon.concat("0");
            } else {
                gamma = gamma.concat("0");
                epsilon = epsilon.concat("1");
            }
        }
        System.out.println(ones);
        System.out.println("Gamma: "+ gamma);
        System.out.println("Epsilon: "+ epsilon);
        System.out.println("Multiplication: " + Integer.parseInt(gamma, 2) * Integer.parseInt(epsilon, 2));
    }

    private void foundOne(Integer position) {
        ones.put(position, ones.getOrDefault(position, 0) + 1);
    }

    private void foundZero(Integer position) {
        ones.put(position, ones.getOrDefault(position, 0) - 1);
    }

}
