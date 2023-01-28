package palankai.io;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import java.util.stream.Stream;

public class LifeSupportRating implements Consumer<String> {
    List<String> startsWith0;
    List<String> startsWith1;
    Strategy strategy;

    public static class Result {
        final List<String> toKeep;
        final String number;

        Result(List<String> toKeep, String number) {
            this.toKeep = toKeep;
            this.number = number;
        }
    }

    public interface Strategy {
        Result forward(List<String> ones, List<String> zeros);
    }

    public static class OxigenStrategy implements Strategy{

        @Override
        public Result forward(List<String> ones, List<String> zeros) {
            if(ones.size()>=zeros.size()) {
                return new Result(ones, "1");
            } else {
                return new Result(zeros, "0");
            }
        }
    }
    public static class CO2Strategy implements Strategy{

        @Override
        public Result forward(List<String> ones, List<String> zeros) {
            if(ones.size()<zeros.size()) {
                return new Result(ones, "1");
            } else {
                return new Result(zeros, "0");
            }
        }
    }

    LifeSupportRating(Strategy strategy) {
        startsWith0 = new ArrayList<>();
        startsWith1 = new ArrayList<>();
        this.strategy = strategy;
    }

    @Override
    public void accept(String s) {
        if(s.charAt(0) == '0') {
            startsWith0.add(s.substring(1));
        } else {
            startsWith1.add(s.substring(1));
        }
    }

    public String result() {
        Result toKeep = this.strategy.forward(startsWith1, startsWith0);
        if(toKeep.toKeep.size() > 1) {
            LifeSupportRating sub = new LifeSupportRating(this.strategy);
            toKeep.toKeep.forEach(sub);
            return toKeep.number + sub.result();
        } else {
            return toKeep.number + toKeep.toKeep.get(0);
        }
    }

    public void summarise() {
        String res = result();
        System.out.println(res + " --> " + Integer.parseInt(res, 2));
    }
}
