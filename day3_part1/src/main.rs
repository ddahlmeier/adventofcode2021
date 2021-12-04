use std::env;
use std::fs;
use std::io::{BufRead, BufReader};

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage day3_part1 <input_file>");
        std::process::exit(1);
    }
    let file = fs::File::open(&args[1]).unwrap();
    let reader = BufReader::new(file);
    let mut report = Vec::new();

    for line in reader.lines() {
        let line = line.unwrap();
        let mut bits = Vec::new();
        for bit in line.chars() {
            bits.push(bit.to_digit(10).unwrap());
        }
        report.push(bits);
    }
    let mut gamma_rate = String::from("");
    let mut epsilon_rate = String::from("");

    let row_count = report.len() as f64;
    for idx in 0..report[0].len() {
        let mut count_ones = 0;
        for line in report.iter() {
           count_ones += line[idx];
        }
        if count_ones as f64 > row_count/2.0 {
            gamma_rate.push('1');
            epsilon_rate.push('0');
        } else {
            gamma_rate.push('0');
            epsilon_rate.push('1');
        }
    }
    let gamma = isize::from_str_radix(&gamma_rate, 2).unwrap();
    let epsilon = isize::from_str_radix(&epsilon_rate, 2).unwrap();
    println!("{}", gamma*epsilon);
}
