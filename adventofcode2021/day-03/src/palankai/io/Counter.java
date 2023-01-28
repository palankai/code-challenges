package palankai.io;

import java.util.function.Consumer;

public class Counter implements Consumer<String> {
    private int count;
    private Integer last;
    Counter() {
        count = 0;
        last = null;
    }
    @Override
    public void accept(String txt) {
        int number = Integer.parseInt(txt);
        if (last != null && last < number) {
            count++;
        }
        last = number;
    }

    public int getCount() {
        return count;
    }
}
