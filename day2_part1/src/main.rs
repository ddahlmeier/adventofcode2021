use std::env;
use std::fs;
use std::io::{BufRead, BufReader};

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage day2:part1 <input_file>");
        std::process::exit(1);
    }
    let file = fs::File::open(&args[1]).unwrap();
    let reader = BufReader::new(file);
    let mut horizontal = 0;
    let mut depth = 0;

    for line in reader.lines() {
        let line = line.unwrap();
        let v: Vec<&str> = line.split(' ').collect();
        let command = v[0];
        let value = v[1].parse::<i32>().unwrap();
        match command {
            "forward"=> horizontal += value,
            "up"=> depth -= value,
            "down"=> depth += value,
            _ =>println!("Unknown command"),
        }
    }
    println!("Result {}", horizontal*depth);
}
