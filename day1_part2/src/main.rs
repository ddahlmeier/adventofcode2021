use std::env;
use std::fs;
use std::io::{BufRead, BufReader};

fn main() {
	let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
    	eprintln!("Usage: day1_part2 <input file>");
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

    	if buffer.len() < 3 {
    		buffer.push(value);
    		continue;
    	}
    	let sum1: i32 = buffer.iter().sum();
		buffer.remove(0);
    	buffer.push(value);
    	let sum2: i32 = buffer.iter().sum();
	
		if sum2 > sum1 {
			increases += 1;
		}
    	
    }
    println!("result {}", increases);
}
