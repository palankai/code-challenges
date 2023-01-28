package palankai;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Vector;

public class Solver {

    public static void main(String[] args) throws IOException {
        String fileName = "input.txt";
        int daysToPass = 256;
        List<String> lines = Files.lines(Paths.get(fileName)).toList();
//        int[] lanternfishes = makeTheListOfNumbers(lines.get(0));
        LanternfishBuckets buckets = new LanternfishBuckets();

        for(int day: makeTheListOfNumbers(lines.get(0))) {
            buckets.addOne(day);
        }

        for(int i=0; i<daysToPass + 1; i++) {
            System.out.printf("Day %s [%s]\n", i, buckets.total());
            buckets.iterateADay();
        }


//        for(int i=0; i<daysToPass + 1; i++) {
//            System.out.printf("Day %s [%s]\n", i, lanternfishes.length);
//            lanternfishes = iterateADay(lanternfishes);
//        }
    }

    public static int[] makeTheListOfNumbers(String line) {
        String[] splitted = line.split(",");
        int[] listOfNumbers = new int[splitted.length];
        for (int i=0; i<splitted.length; i++) {
            listOfNumbers[i] = Integer.parseInt(splitted[i]);
        }
        return listOfNumbers;
    }

    public static int[] iterateADay(int[] lanternfishes) {
        int zeros = 0;
        for(int i=0; i<lanternfishes.length; i++) {
            if (lanternfishes[i] == 0) {
                lanternfishes[i] = 6;
                zeros++;
            } else {
                lanternfishes[i]--;
            }
        }
        int[] nextDayLanternFishes = Arrays.copyOf(lanternfishes, lanternfishes.length + zeros);
        for(int i=0; i<zeros; i++) {
            nextDayLanternFishes[nextDayLanternFishes.length - i - 1] = 8;
        }
        return nextDayLanternFishes;
    }


}
