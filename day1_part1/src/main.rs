use std::env;
use std::fs;
use std::io::{BufRead, BufReader};

fn main() {
	let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
    	eprintln!("Usage: day1_part1 <input file>");
    	std::process::exit(1);
    }
    let filename = &args[1];
    let file = fs::File::open(filename).unwrap();
    let reader = BufReader::new(file);
    let mut buffer: Vec<i32> = Vec::new();
    let mut increases = 0;

    for line in reader.lines() {
    	let line = line.unwrap();
    	let value = line.parse::<i32>().unwrap();
    	buffer.push(value);

    	if buffer.len() < 2 {
    		continue;
    	}
    	if buffer[1] > buffer[0] {
    		increases += 1;
    	}
    	buffer.remove(0);
    }
    println!("result {}", increases);
}
