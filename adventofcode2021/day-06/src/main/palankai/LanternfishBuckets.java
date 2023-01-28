package palankai;

import java.util.Arrays;

public class LanternfishBuckets {
    long[] buckets = new long[9];

    LanternfishBuckets() {
        Arrays.fill(buckets, 0);
    }

    public void addOne(int day) {
        buckets[day] ++;
    }

    public void iterateADay() {
        long regenerate = buckets[0];
        for(int i=0; i<buckets.length-1; i++) {
            buckets[i] = buckets[i+1];
        }
        buckets[6] = buckets[6] + regenerate;
        buckets[buckets.length-1] = regenerate;
    }

    public long total() {
        long total = 0;
        for (long bucket : buckets) {
            total += bucket;
        }
        return total;
    }

    @Override
    public String toString() {
        return Arrays.toString(buckets);
    }

}
