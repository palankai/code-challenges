package palankai.io;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.function.Consumer;
import java.util.stream.Stream;

public class Main {

    public static void main(String[] args) throws IOException {
        String fileName = "input.txt";
        Main main = new Main(fileName);
        main.solve();
    }

    private final String fileName;

    Main(String fileName) {
        this.fileName = fileName;
    }

    public void solve() throws IOException {
        Stream<String> lines = Files.lines(Paths.get(this.fileName));
        LifeSupportRating counter = new LifeSupportRating(new LifeSupportRating.OxigenStrategy());
        lines.forEach(counter);
        counter.summarise();

        Stream<String> lines2 = Files.lines(Paths.get(this.fileName));
        LifeSupportRating counter2 = new LifeSupportRating(new LifeSupportRating.CO2Strategy());
        lines2.forEach(counter2);
        counter2.summarise();
    }

}
