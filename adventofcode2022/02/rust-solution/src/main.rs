use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("example.txt")?;
    let reader = BufReader::new(file);

    for line in reader.lines() {
        let safe_line = line.expect("It should have been a string");
        let split = safe_line.split(" ");
        let vec: Vec<&str> = split.collect();

        println!("{} vs {}", vec[0], vec[1])
    }

    Ok(())
}

